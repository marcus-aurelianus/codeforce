import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce


def gift():
    for _ in range(t):
        n,k=list(map(int,input().split()))
        array=list(map(int,input().split()))

        zrem=0

        dic={}
        for i in range(n):
            rem=array[i]%k
            if rem:
                freq=dic.get(rem,0)
                dic[rem]=freq+1
        if dic:
            val=max(dic, key=dic.get)
            dicval=dic[val]

            minlst=[]
            for key in dic:
                if dic[key]==dicval:
                    minlst.append(key)


            minlst.sort()
            minitem=minlst[0]
            yield dic[minitem]*k-(minitem-1)
        else:
            yield 0
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
