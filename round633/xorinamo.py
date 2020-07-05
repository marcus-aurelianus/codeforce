import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


art=[1,2,3,4,8,12,5,10,15,6,11,13]
for ele in art:
    print((12-len(bin(ele)[2:]))*'0'+bin(ele)[2:])
n=int(input())
arry=list(map(int,input().split()))
