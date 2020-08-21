import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry= list(map(int,input().split()))

        prev=arry[n-1]
        increase=True

        res=None
        for i in range(n-1):
            curr=arry[n-2-i]
            if curr>prev:
                if increase:
                    prev=curr
                    continue
                else:
                    res=i
                    break
            elif curr==prev:
                prev=curr
                continue
            else:
                if increase:
                    prev=curr
                    increase=False
                else:
                    prev=curr
                    continue
        if res:
            yield n-res-1
        else:
            yield 0
                    
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
