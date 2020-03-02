import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,initemp= map(int,input().split())
        res=True
        temprange=[initemp,initemp]
        prevtime=0
        for _ in range(n):
            if res:
                time,lower,upper=map(int,input().split())
                prevlow,prevup=temprange
                nowlow,nowup=prevlow-(time-prevtime),prevup+(time-prevtime)
                #print(nowlow,nowup)
                if nowlow<lower:
                    fixlow=lower
                    if nowup<lower:
                        fixup=nowup
                        res=False
                    else:
                        if nowup>upper:
                            fixup=upper
                        else:
                            fixup=nowup
                elif nowlow>upper:
                    fixlow,fixup=nowlow,nowup
                    res=False
                else:
                    fixlow=nowlow
                    if nowup>upper:
                        fixup=upper
                    else:
                        fixup=nowup
                #print(fixlow,fixup)
                temprange=[fixlow,fixup]
                prevtime=time
            else:
                kappa=input()
        if res:
            yield 'YES'
        else:
            yield 'NO'
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
        
    
