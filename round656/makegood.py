import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry= list(map(int,input().split()))
        s,e=0,n-1
        curr=-1
        while True and s<=e:
            found=False
            if arry[s]>arry[e]:
                if arry[e]>=curr:
                    curr=arry[e]
                    e-=1
                    found=True
                elif arry[s]>=curr:
                    curr=arry[s]
                    s+=1
                    found=True
            else:
                if arry[s]>=curr:
                    curr=arry[s]
                    s+=1
                    found=True
                elif arry[e]>=curr:
                    curr=arry[e]
                    e-=1
                    found=True
            if not found:
                break

        yield e-s+1
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
