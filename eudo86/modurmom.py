import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        a,b,q=map(int,input().split())
        lcm=a*b//math.gcd(a,b)
        maxdog=max(a,b)
        for i in range(q):
            
            s,e=map(int,input().split())
            ans=(e-s+1)

            startq,startm=s//lcm,s%lcm
            endq,endm=e//lcm,e%lcm
            if startq==endq:
                if startm<maxdog:
                    if endm<maxdog:
                        ans-=(endm-startm+1)
                    else:
                        ans-=(maxdog-startm)
            else:
                if startm<maxdog:
                    ans-=(maxdog-startm)
                #print(ans)
                ans-=((endq-startq-1)*maxdog)
                if endm<maxdog:
                    ans-=(endm+1)
                else:
                    ans-=maxdog
            yield ans

                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
