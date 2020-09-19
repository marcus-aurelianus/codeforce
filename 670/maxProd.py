import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def sumP(arry):
    ans=1
    for ele in arry:
        ans*=ele
    return  ans
def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        array.sort()
        if n==5:
            yield sumP(array)
        else:
            poss=[0]*6
            for i in range(6):
                poss[i] = sumP(array[:i])*sumP(array[n-(5-i):])
            yield max(poss)  
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
