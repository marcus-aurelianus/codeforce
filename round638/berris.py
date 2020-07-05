import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,k = list(map(int,input().split()))


ans=0
prema,premb=0,0
comrem=0
for i in range(n):
    r,b = list(map(int,input().split()))
    quo=(r+b)//k
    rem=(r+b)%k
    ans+=quo
    if quo==0:
        premb+=b
        prema+=r
    elif rem>r:
        premb+=(rem-r)
        comrem+=r
    elif rem>b:
        prema+=(rem-b)
        comrem+=b
    else:
        comrem+=rem
    #print(comrem)
#print(prema,premb,comrem)
ans+=comrem//k
comrem=comrem%k

ans+=premb//k
premb=premb%k

ans+=prema//k
prema=prema%k

if comrem+premb>=k:
    ans+=1
    comrem=comrem+premb-k
if comrem+prema>=k:
    ans+=1
    comrem=comrem+prema-k
            
print(ans)
