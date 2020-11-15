import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

n = int(input())
items = list(map(int,input().split()))
count=0
for x in items:
    if ((x != 1) and (x != 0) and ((x & (x - 1)) == 0)):
        count+=1
print(count)

#1+2
#"{} {} {}".format(maxele,minele,minele)
# 1 2 3 4
# 10 9 8 7

# 1 2 3 4

# 9 2 3 4
# 8 1 3 4
# 7 1 2 4
# 6 1 2 3

# 1 2 3
# 1 3 4
# 3 3 6
# 6 6 6
