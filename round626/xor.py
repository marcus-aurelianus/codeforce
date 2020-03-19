import sys
from math import gcd
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



if __name__ == '__main__':
    n=int(input())
    arry = list(map(int, sys.stdin.readline().split()))
    res=0
    for i in range(n):
        for j in range(i+1,n):
            res^=(arry[i]+arry[j])
    print(res)

