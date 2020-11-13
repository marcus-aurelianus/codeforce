import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from copy import deepcopy
def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        dic = {}
        for ele in arry:
            ans = dic.get(ele,False)
            if ans:
                break
            else:
                dic[ele]=True
        if ans:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
