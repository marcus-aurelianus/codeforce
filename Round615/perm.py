import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

stk=[]
n,m=map(int,input().split())
for i in range(n):
    stk.append(list(map(int,input().split())))
print(stk)
