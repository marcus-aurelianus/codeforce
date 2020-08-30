import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from bisect import bisect_left

n,m = list(map(int,input().split()))

cons=1000000
HarrL=[]
HarrR=[]
ans=1
for i in range(n):
    arry = list(map(int,input().split()))
    if arry[1]==0:
        if arry[2]==cons:
            ans+=1
        HarrL.append(arry)
    else:
        HarrR.append(arry)
HarrL.sort(key=lambda x:x[2])
leftstart=list(map(lambda x:x[2],HarrL))
n1=len(HarrL)
HarrR.sort(key=lambda x:x[1])
rightstart=list(map(lambda x:x[1],HarrR))
n2=len(HarrR)
#print(HarrL,HarrR,leftstart,rightstart)
for i in range(m):
    arry = list(map(int,input().split()))
    #print(i,arry,ans)
    if arry[1]==0:
        if arry[2]==cons:
            ans+=1
        if n==0:continue
        tem=bisect_left(leftstart,arry[0])

        for j in range(tem,n1):
            if HarrL[j][0]<=arry[2]:
                ans+=1
        #print(rightstart,arry[0])
        tem1=bisect_left(rightstart,arry[0])
        if tem1==0 and rightstart[tem1]>arry[0]:
            continue
        if tem1!=0:
            tem1-=1
        for j in range(tem1,n2):
            #print(HarrR[j][1],arry[1])
            if HarrR[j][1]<=arry[2]:
                
                ans+=1       
    else:
        if n==0:continue
        tem=bisect_left(leftstart,arry[0])

        for j in range(tem,n1):
            if arry[1]<=HarrL[j][2]:
                ans+=1
        #print(ans)
        tem1=bisect_left(rightstart,arry[0])
        #print(tem1)
        if tem1==0 and rightstart[tem1]>arry[0]:
            continue
        for j in range(tem1,n2):
            if arry[1]<=HarrR[j][1]:
                ans+=1          

print(ans)

#"{} {} {}".format(maxele,minele,minele)
