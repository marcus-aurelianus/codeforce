import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string = input()
        n = len(string)
        if n==1:
            yield 0
        else:
            ans = 0
            if n%2:
                toEnd = n//2+1
                toStart = n//2-1
            else:
                toEnd = n//2
                toStart = n//2-1                
            while toEnd<n-1:
                if string[toEnd]==string[toEnd+1]:
                    ans+=1
                toEnd+=1
            while toStart>0:
                if string[toStart]==string[toStart-1]:
                    ans+=1
                toStart-=1


            if n%2:
                if string[n//2]==string[n//2-1] and ((n>3 and string[n//2]!=string[n//2-2]) or (n==3)) :
                    ans+=1
                if string[n//2]==string[n//2+1] and ((n>3 and string[n//2]!=string[n//2+2]) or (n==3)):
                    ans+=1
            else:
                if string[n//2]==string[n//2-1] and (string[n//2]!=string[n//2+1] or string[n//2-1]!=string[n//2-2]) and n>=4:
                    ans+=1
            rev = True
            for i in range(n):
                if string[i]!=string[n-1-i]:
                    rev=False
                    break
            if ans==0 and rev:
                ans+=1
            yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
# baebdcb
