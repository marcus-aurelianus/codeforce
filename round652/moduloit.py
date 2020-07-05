import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
mod=10**9+7
def gift():
    for _ in range(t):
        n=int(input())
        if n<=2:
            yield 0
        elif n<=4:
            yield 4
        else:
            curs=4
            tobecome=4

            for i in range(5,n+1):
                temp=tobecome
                

                tobecome=tobecome+curs*2
                if (i-6)%3==0:
                    tobecome+=4
                tobecome%=mod
                curs=temp
            yield (tobecome)%mod

                    

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
