import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
m,n=[int(ele) for ele in input().split()]
a=[]
for i in range(m):
    a.append(list(map(int, input().split())))


ina,mo=0,10**9+1
pos1,pos2=0,0
mask=(1<<n)-1
def check(tang):
    key=set()
    dic=dict()
    for i in range(m):
        temp=0 
        for j in range(n):
            if a[i][j]>=tang:
                #print("ya")
                temp+=(1<<j)
        #print(bin(temp),a[i],tang)
        if temp in key:
            continue
        key.add(temp)
        tempk=temp
        while tempk>=0:
            tempk &= temp
            dic[tempk]=i
            tempk-=1
            
        tocheck = mask ^ temp
        #print(bin(tocheck),bin(temp),bin(mask),a[i],tang)

        if tocheck in dic:
            return dic[tocheck],i,True

    #print(dic)
    return -1,-1,False
        
while ina<mo-1:
    #print(ina,mo)
    tang=(ina+mo)//2
    #print(ina,mo,tang)
    temppos1,temppos2,status=check(tang)
    #print(status)
    if status:
        pos1,pos2=temppos1,temppos2
        ina=tang
    else:
        mo=tang
print(pos1+1,pos2+1)
    
