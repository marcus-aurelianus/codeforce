a=[ 60,55,50,10]

res=(a[0]|a[1])-min(a[0],a[1])
temp=[a[0],a[1]]
for i in range(1,len(a)):
    t1,t2=temp
    prob1=(a[i]|t1)-min(a[i],t1)
    prob2=(a[i]|t2)-min(a[i],t2)
    print(t1,t2,prob1,prob2)
    if prob1>prob2 and prob1>res:
        res=prob1
        temp=[a[i],t2]
    elif prob2>prob1 and prob2>res:
        res=prob2
        temp=[t1,a[i]]
print(temp)
