import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        ## n**2-n-2b=0
        ## 1+(1+9b)/2
        ##
        pos1=math.ceil((-1+((1+8*b))**0.5)/2)
        pos2=b-(pos1**2-pos1)//2
        ans=''
        
        
        
        
        ans+=(a-(pos2)-(pos1-pos2+1))*'a'
        ans+='b'
        ans+=(pos1-pos2)*'a'
        ans+='b'
        ans+=(pos2-1)*'a'
        yield ans
     
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
