import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(rev):
        n,k=list(map(int,input().split()))
        a=list(map(int,input().split()))


        imos = [0]*(2*k+2)
        for i in range(n//2):
            s = a[i]
            t = a[n-1-i]
            s, t = min(s, t), max(s, t)
            l=s+1
            m=s+t
            r=t+k
            imos[l] -=1
            imos[m] -= 1
            imos[m+1] += 1
            imos[r+1] +=1
            imos[1] += 2


 
        for i in range(1, 2*k+2):
            imos[i] += imos[i-1]
        ans = 10**18
        
        for i in range(1, 2*k+1):
            ans = min(ans, imos[i])
        yield ans
                 
if __name__ == '__main__':
    rev= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
 
