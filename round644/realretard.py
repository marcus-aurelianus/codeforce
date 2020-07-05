import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        arry.sort()
        mindiff=float("inf")
        for i in range(n-1):
            diff=abs(arry[i+1]-arry[i])
            mindiff=min(mindiff,diff)
        yield mindiff
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
