import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry= list(map(int,input().split()))
        blocks=[]
        temp=arry[0]
        ans=True
        for i in range(1,n):
            curr=arry[i]
            prev=arry[i-1]
            if curr<prev:
                if curr>temp:
                    ans=False
                    break
                else:
                    temp=curr
            else:
                if curr-prev!=1:
                    ans=False
                    break
        if ans:
            yield 'Yes'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
