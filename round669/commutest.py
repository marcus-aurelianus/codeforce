import sys
from itertools import permutations 
from random import randint
orilst=list(range(1,10001))
for i in range(10000):
    start = randint(0,9999)
    end = randint(0,9999)
    orilst[start],orilst[end]=orilst[end],orilst[start]
kap = [orilst]
n=len(orilst)
counter=0

quries = 0
for lst in kap:
    if n==1:
        print("! 1",flush = True)
    else:
        arry = [0]*n
        pos = None

        start = 0
        end = 1

        quried = 1
        while quried<n:
            ans1=lst[start]%lst[end]
            ans2=lst[end]%lst[start]
            if ans1>ans2:
                arry[start]=ans1
                start = end
                end = (end+1)%n
            else:
                arry[end]=ans2
                end = (end+1)%n
            
            quried+=1
            quries+=2
            
        if start == end:
            arry[start]=n
        else:
            ans1=lst[start]%lst[end]
            ans2=lst[end]%lst[start]
            if ans1>ans2:
                arry[start]=ans1
                arry[end]=n
            else:
                arry[end]=ans2
                arry[start]=n
            quries+=2
        if arry!=list(lst):
            print ("! {}".format(" ".join(str(x) for x in arry)) , flush = True)

        counter+=1
print(quries)
