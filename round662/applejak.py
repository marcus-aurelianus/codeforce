import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n=int(input())

lis=[0]*(10**5+1)

arry=list(map(int,input().split()))

m=int(input())

two=0
four=0

for i in range(n):
    lis[arry[i]]+=1
    if lis[arry[i]]%2==0:
        two+=1
    if lis[arry[i]]%4==0:
        four+=1

for i in range(m):
    sign,numstr=input().split()
    if sign=="+":
        lis[int(numstr)]+=1
        if lis[int(numstr)]%2==0:
            two+=1
        if lis[int(numstr)]%4==0:
            four+=1
    else:
        
        if lis[int(numstr)]%2==0:
            two-=1
        if lis[int(numstr)]%4==0:
            four-=1
        lis[int(numstr)]-=1
    #print(two,four)
    if four>=1 and two>=4:
        print('YES')
    else:
        print('NO')



#"{} {} {}".format(maxele,minele,minele)
