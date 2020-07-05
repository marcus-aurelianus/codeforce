import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        granny = list(map(int,input().split()))
        granny.sort()
        ans=1
        for i in range(n):
            currgr=granny[n-1-i]
            #print(currgr)
            if currgr<=n-i:
                ans=n-i+1
                break
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
