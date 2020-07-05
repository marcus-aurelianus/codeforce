import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        ans=0
        dis=(n+1)//2
        for i in range(1,dis):
            ans+=((i*2)*4)*(i)
        yield ans
        


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
