import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n=int(input())
arry = list(map(int,input().split()))



ans=[]

##arrangepoint=[]
##for i in range(n):
##
##    if arry[i]==i+1:
##        arrangepoint.append(i)
dic={}
toreach='notyet'
for i in range(n):
    curr=arry[n-1-i]

    gotans=False

    if toreach=='notyet':
        toreach=curr-1
    loumou=False
    if i<n-1:
        prevele=arry[n-2-i]
        if prevele<curr:
            gotans=True
            ans=[prevele]+ans
            dic[prevele]=True
        elif prevele==curr:
            loumou=True

    if not gotans:
        foundpoint='no'

        
        while True:
            if toreach<0:
                break
            else:
                ina=dic.get(toreach,False)
                if not ina:
                    foundpoint=toreach
                    if n-i==foundpoint:
                        dic[foundpoint]=True
                    break
            toreach-=1
        if foundpoint=='no':
            ans=[n]+ans
        else:
            ans=[foundpoint]+ans
    #print(i,dic,ans)

if arry[0]==1:
    ans[0]=0
elif arry[0]==0:
    ans[0]=1

print(" ".join(str(x) for x in ans))

