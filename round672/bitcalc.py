import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))

        dic = defaultdict(lambda:0)
        for ele in arry:
            dic[len(bin(ele))]+=1
        ans = 0
        for k,v in dic.items():
            ans += ((v-1)*v)//2
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
