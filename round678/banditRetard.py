import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

people = int(input())
roads = list(map(int,input().split()))
citizens = list(map(int,input().split()))

dic = {1:True}
uniq = 0
for i,ele in enumerate(roads):
    curr = i+2
    dic[curr]=True
    dic[ele]=False

maxAns = 0
for ele in dic:
    if dic[ele]:
        uniq+=1
        maxAns = max(maxAns,citizens[ele-1])

print(max(maxAns,math.ceil(sum(citizens)/uniq)))
#"{} {} {}".format(maxele,minele,minele)
# 1 2 2 2 2
