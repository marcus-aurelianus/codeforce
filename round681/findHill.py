import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if n<=2:
            yield 'YES'
        else:
            s,e = 1,n-2

            while s<e:
                found=False
                if a[s]<=a[s-1]:
                    s+=1
                    found=True
                if a[e]<=a[e+1]:
                    e-=1
                    found=True
                if not found:
                    break
            if s>=e:
                yield 'YES'
            else:
                currS = a[s-1]
                if e+1>n-1:
                    currE = a[n-1]
                else:
                    currE = a[e+1]
                #print(a,a[s:e+1],s,e)
                rev = False
                count = 0
                for i in range(s,e+1):
                    if a[i]<a[i-1]:
                        if not rev:
                            rev=not rev
                    elif a[i]>a[i+1]:
                        if rev:
                            count+=1
                            rev=not rev
                #print(count,a[s:e+1])
                if count<=1 and max(a[s:e+1])<=currS+currE:
                    yield 'YES'
                else:
                    yield 'NO'
                    
                        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
