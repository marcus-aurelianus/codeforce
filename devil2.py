t=int(input())
lst=[int(ele) for ele in input().split()]


maxn=max(lst)

n=len(bin(maxn)[2:])
newlst=["0"*(n-len(bin(ele)[2:]))+bin(ele)[2:] for ele in lst]

res=['0']*n

def countzeroOne(lstrino,loc):
    count0=0
    count1=0
    temp1,temp2=[],[]
    for lst1 in newlst:
        if lst1[loc]=='0':
            count0+=1
            temp1.append(lst1)
        else:
            count1+=1
            temp2.append(lst1)
    oinOne,oinTwo=False,False
    zinOne,zinTwo=False,False
    max1,max2=0,0
    for ele in temp1:
        max1=max(max1,int(ele[loc+1:],2))
        if ele[loc+1]=='1':
            oinOne=True
        else:
            zinOne=True
    for ele in temp2:
        max2=max(max2,int(ele[loc+1:],2))
        if ele[loc+1]=='1':
            oinTwo=True
        else:
            zinTwo=True
    return count0,count1,zinOne and oinOne,zinTwo and oinTwo,temp1,temp2,max1>max2
marker=False
for i in range(n-1):
    count0,count1,inOne,inTwo,temp1,temp2,checker=countzeroOne(newlst,i)
    #print(i,newlst,res,count1,inOne,inTwo)
    if count1==1:
        if not marker and count0>0:
            res[i]='1'
            marker=True
        break
    elif count1==0:
        continue
    else:
        if count0>0:
            if not marker:
                res[i]='1'
                marker=True
            if inOne and inTwo:
                if checker:
                    marker=False
                    newlst=temp2
                else:
                    marker=False
                    newlst=temp2
            if inOne:
                marker=False
                newlst=temp2
            elif inTwo:
                marker=False
                newlst=temp1
    

print(int("".join(res),2))       
