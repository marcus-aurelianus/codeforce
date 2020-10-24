import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,x,pos = list(map(int,input().split()))

mod = 10**9 + 7
ans = 1

left = 0
right = n

counter = 0
bigger = n-x
smaller = x-1
while left<right:
    middle = (left+right)//2
    #print(left,right,pos)
    if middle>pos:
        if bigger>0:
            ans = ans*(bigger)%mod
            bigger-=1
            right = middle
        else:
            ans = 0
            break
    elif middle<pos:
        if smaller>0:
            ans = ans*(smaller)%mod
            smaller-=1
            left = middle + 1
        else:
            ans = 0
            break
    else:
        break
if ans == 0:
    print(0)
else:
    for i in range(1,bigger+smaller+1):
        ans = ans*(i)%mod
    print(ans)


#"{} {} {}".format(maxele,minele,minele)
# 1 2 2 2 2
