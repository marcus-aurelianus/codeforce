import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        a,b,k = list(map(int,input().split()))
        boys = list(map(int,input().split()))
        girls = list(map(int,input().split()))
        boydic = defaultdict(list)
        girldic = defaultdict(list)
        for i in range(k):
            boy,girl=boys[i],girls[i]
            boydic[boy].append(girl)
            girldic[girl].append(boy)
        ans = 0
        #print(boydic,girldic)
        for i in range(k):
            boyRelated = len(boydic[boys[i]])
            girlRelated = len(girldic[girls[i]])
            ans += max(0,k-boyRelated-girlRelated+1)
        yield ans//2
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
