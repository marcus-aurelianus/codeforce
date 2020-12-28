import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string = input()
        
        n = len(string)
        if n%2:
            yield 'NO'
        else:
            lans = True
            left,q =0,0
            for i in range(n):
                if string[i]=='?':
                    if left==0:
                        left+=1
                    else:
                        q+=1
                elif string[i]=='(':
                    left+=1
                else:
                    if left>0:
                        left-=1
                    elif q>0:
                        q-=1
                    else:
                        lans = False
                        break

            rans = True
            left,q =0,0
            for i in range(n):
                if string[n-1-i]=='?':
                    if left==0:
                        left+=1
                    else:
                        q+=1
                elif string[n-1-i]==')':
                    left+=1
                else:
                    if left>0:
                        left-=1
                    elif q>0:
                        q-=1
                    else:
                        rans = False
                        break
            if lans and rans:
                yield 'YES'
            else:
                yield 'NO'
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
