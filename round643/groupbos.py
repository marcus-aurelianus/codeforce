import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        dudes = list(map(int,input().split()))
        dudes.sort()
        ans=0
        cur=0
        for dud in dudes:
            cur+=1
            if cur==dud:
                ans+=1
                cur=0
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
