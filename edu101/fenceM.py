import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        heights = list(map(int,input().split()))
        ans=True
        minV,maxV = heights[0],heights[0]+k-1
        for i in range(1,n):
            prev,curr = heights[i-1],heights[i]
            if curr>prev:
                if abs(curr-maxV)>k-1:
                    ans=False
                    break
                else:
                    minV=curr
                    maxV=maxV-1+k
            else:
                if abs(minV-(curr+k-1))>k-1:
                    ans=False
                    break
                else:
                    minV=minV+1-k
                    maxV=curr+k-1
            if maxV<minV:
                ans=False
                break
            
        if not ans:
            yield 'NO'
        else:
            if minV<=heights[-1]<=maxV:
                yield 'YES'
            else:
                yield 'NO'
            
 
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
