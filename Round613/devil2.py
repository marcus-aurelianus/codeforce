t=int(input())
lst=[int(ele) for ele in input().split()]


maxn=max(lst)

n=len(bin(maxn)[2:])
newlst=["0"*(n-len(bin(ele)[2:]))+bin(ele)[2:] for ele in lst]

def catchEvil(lstrino,loc):
    count0,count1=[],[]
    for ele in lstrino:
        if ele[n-1-loc]=='1':
            count1.append(ele)
        else:
            count0.append(ele)
    if len(count0)==0:
        if loc==0:
            return 0
        else:
            return catchEvil(lstrino,loc-1)
    elif len(count1)==0:
        if loc==0:
            return 0
        else:
            return catchEvil(lstrino,loc-1)
    else:
        if loc==0:
            return 1
        else:
            return min(catchEvil(count1,loc-1),catchEvil(count0,loc-1))+(1<<loc)


if  n==0:
    print(0)
else:
    print(int(catchEvil(newlst,n-1)))  
    
