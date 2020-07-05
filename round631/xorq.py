import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        ns=format(n,'b')
        ans=0
        for i in range(len(ns)):
            if i!=len(ns)-1:
                ans+=(ans+1)*(2**i)
            else:
                ans+=(ans+1)*(n-2**i+1)
            ans%=m
        yield ans


            
                
                    
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
