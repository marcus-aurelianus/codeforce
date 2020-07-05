import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
              
if __name__ == '__main__':
    n,k=map(int,input().split())
    arryn=list(map(int,input().split()))
    arryc=list(map(int,input().split()))
    curlen=1
    counterdude=[0]*k
    counterdude[arryn[0]-1]=1
    for i in range(1,n):
        ele=arryn[i]
        counterdude[ele-1]+=1
    anslen=(counterdude[k-1]//arryc[k-1])
    if counterdude[k-1]%arryc[k-1]:
        anslen+=1
    for i in range(k-2,-1,-1):
        counterdude[i]+=counterdude[i+1]

        tisinamo=(counterdude[i]//arryc[i])
        if counterdude[i]%arryc[i]:
            tisinamo+=1
        anslen=max(anslen,tisinamo)
    ans=[]
    for  i in range(anslen):
        ans.append([])
    #print(counterdude)
    for i in range(k):
        if i==0:
            tisele=counterdude[k-i-1]
            slen=0
            spoint=0
            canlen=tisele//arryc[k-i-1]
            rem=tisele%arryc[k-i-1]
        else:
            tisele=counterdude[k-i]-counterdude[k-i-1]
            slen=counterdude[k-i]//arryc[k-i-1]
            #print(counterdude[k-i],arryc[k-i-1],counterdude[k-i]//arryc[k-i-1])
            spoint=counterdude[k-i]%arryc[k-i-1]
            canlen=(counterdude[k-i-1])//arryc[k-i-1]
            rem=counterdude[k-i-1]%arryc[k-i-1]
        if tisele:
            if spoint!=0:
                if slen<canlen:
                    ans[slen]+=[k-i]*(arryc[k-i-1]-spoint)
                else:
                    ans[slen]+=[k-i]*(spoint)
                slen+=1
            #print(k-i,slen,canlen,ans,canlen,spoint)
            for j in range(slen,canlen):
                ans[j]+=[k-i]*arryc[k-i-1]
            #print(ans) 
            if rem and canlen>=slen:
                ans[canlen]+=[k-i]*rem
        #print(ans) 
    print(len(ans))
    for dude in ans:
        print(str(len(dude))+" "+" ".join(str(x) for x in dude))
