import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


palin={}
alone=None
droed=""
n,len1=map(int,input().split())

for i in range(n):
    str1=input()
    reverserino=str1[::-1]
    findrever=palin.get(reverserino,0)
    if findrever:
        droed=str1+droed
        droed=droed+reverserino
        findrever-=1
        palin[reverserino]-=1
        if alone==reverserino and findrever==1:
            alone==None
    else:
        freq=palin.get(str1,0)
        palin[str1]=freq+1
        if str1==reverserino:
            if alone==None:
                alone=str1

if alone:
    lenrino=len(droed)//2
    res=droed[:lenrino]+alone+droed[lenrino:]
    print(len(res))
    print(res)
else:
    print(len(droed))
    print(droed)

        
    
