import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n= int(input())
            
ans = [4,4,12,9]

if n<=4:
    print(ans[n-1])
else:
    for i in range(4,n):
        toPlus = ((i)//2+1)*4
        if i%2==0:
            ans.append(ans[i-2]+toPlus)
        else:
            ans.append(ans[i-4]+toPlus)
    print(ans[-1])
#"{} {} {}".format(maxele,minele,minele)





# 4 4 12 9 24  16 40   25  60
#     +8   +12 +12 +16 +16 +20
