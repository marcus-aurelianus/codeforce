import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k=map(int,input().split())
        if k%(n-1):
            yield k//(n-1)*n+(k%(n-1))
        else:
            yield k//(n-1)*n-1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')



##100 55
##1 3 5
##33  22

##x+3*(k-x)=n
##n=3*k-2*x
##x=(3*k-n)//2
##1 3 1 3 1 3 49
            
