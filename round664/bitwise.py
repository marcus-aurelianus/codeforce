import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,m= list(map(int,input().split()))

arrayA = list(map(int,input().split()))
arrayB = list(map(int,input().split()))

curr=[0]*9
minarr=[]
didiarr=[]
arrayA.sort(reverse=True)
for i in range(n):
    
    minval=float("inf")
    index=None
    for j in range(m):
        curlis=list((9-len(bin(arrayA[i]&arrayB[j])[2:]))*'0'+bin(arrayA[i]&arrayB[j])[2:])
        newNum=[0]*9
        for k in range(9):
            if curlis[k]=='1' and curr[k]!=1:
                newNum[k]=1

        realNum=int(''.join(str(x) for x in newNum),2)
        if realNum<minval:
            index=j
            minval=realNum
        #print(curlis)
    
    curlis=list((9-len(bin(arrayA[i]&arrayB[index])[2:]))*'0'+bin(arrayA[i]&arrayB[index])[2:])
    #print(curlis,arrayA[i]&arrayB[index])
    for d in range(9):
        if curlis[d]=='1':
            curr[d]=1
    #print(curr)
    minarr.append(arrayA[i]&arrayB[index])

ans=minarr[0]

for i in range(1,n):
    ans|=minarr[i]



print(ans)
        
