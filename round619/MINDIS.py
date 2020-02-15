import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def birth():
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        inamo=[]
        maxdis=0
        for i in range(n):
            if i<n-1:
                #print(a[i]!=-1,a[i+1]!=-1)
                if a[i]!=-1 and a[i+1]!=-1:
                    #print(maxdis,a[i+1]-a[i])
                    maxdis=max(maxdis,abs(a[i+1]-a[i]))
            if a[i]==-1:
                if i==0:
                    if a[i+1]!=-1:
                        if a[i+1] not in inamo:
                            inamo.append(a[i+1])
                elif i==n-1:
                    if a[i-1]!=-1:
                        if a[i-1] not in inamo:
                            inamo.append(a[i-1])
                else:
                    if a[i+1]!=-1:
                        if a[i+1] not in inamo:
                            inamo.append(a[i+1])
                    if a[i-1]!=-1:
                        if a[i-1] not in inamo:
                            inamo.append(a[i-1])
            
        if inamo:
            #print(maxdis,inamo)
            res=(max(inamo)+min(inamo))//2
            maxlen=max(max(max(inamo)-res,res-min(inamo)),maxdis)
            yield str(maxlen)+" "+str(res)
        else:
            yield "0 0"
        
                        
if __name__ == '__main__':
    t= int(input())
    ans = birth()
    print(*ans,sep='\n')
            
