import sys
n = int(input())

total=[]
fHalf={}
shalf={}

if n==1:
    query = "? 1 1"
    print (query, flush = True)
    res=None
    for i in range(2):
        temp=input()
        if len(temp)==1:
            res=temp
    print ("!" , res , flush = True)    
else:
    m=n//2
    query = "? 1 "+ str(m)

    print (query, flush = True)

    freq1=(m+1)*m//2+1

    for i in range(freq1):
        tempstr=input()
        if len(tempstr)==m:
            fHalf[tempstr]=True 


    query = "? "+ str(m+1)+" "+str(n)

    print (query, flush = True)


    freq2=((n-m)+1)*(n-m)//2+1
    for i in range(freq1):
        tempstr=input()
        if len(tempstr)==n-m:
            shalf[tempstr]=True 


    query = "? 1 "+ str(n)

    print (query, flush = True)

    freq3=((n)+1)*(n)//2+1
    for i in range(freq3):
        tempstr=input()
        if len(tempstr)==n:
            total.append(tempstr)
    res=None
    print(total)
    for ele in total:
        fhT=fHalf.get(ele[:m],False)
        shT=shalf.get(ele[m:],False)
        if fhT and shT:
            res=ele
            break
    print ("!" , res , flush = True)

    
    
