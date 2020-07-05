import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n0,n1,n2=list(map(int,input().split()))
        ans=''
        if n0>0:
            ans='0'+'0'*(n0)
        if n1>0:
            if ans=='':
                ans+='0'
            if n1%2==0:
                ans='1'+ans
                ans+='1'
                ans+='01'*(n1//2-1)
            else:
                ans+='1'
                ans+='01'*((n1+1)//2-1)
        if ans=='':
            ans+='1'
        ans+='1'*(n2)
        yield ans            
                
            
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
            
