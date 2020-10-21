import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        gangs = list(map(int,input().split()))
        dic = defaultdict(lambda:[])
        for i,ele in enumerate(gangs):
            dic[ele].append(i)
        maxele = max(dic, key=lambda k: len(dic[k]))
        if len(dic[maxele])==n:
            yield 'NO'
        else:
            yield 'YES'
            topele = gangs[0]
            foundele = None
            toConnec = []
            for i in range(1,n):
                if gangs[i]!=topele:
                    yield "{} {}".format(1,i+1)
                    if foundele==None:
                        foundele = i+1
                else:
                    toConnec.append(i+1)
            for ele in toConnec:
                yield "{} {}".format(foundele,ele)
         
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
