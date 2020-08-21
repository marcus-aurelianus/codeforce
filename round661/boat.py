import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))

        finalans=0
        kap=max(arry)
        bibi=min(arry)
        for i in range(bibi+1,kap*2+1):
            dic=defaultdict(lambda:0)
            ans=0
            for ele in arry:
                if i>ele:
                    if dic[i-ele]>0:
                        dic[i-ele]-=1
                        ans+=1
                    else:
                        dic[ele]+=1
            finalans=max(finalans,ans)
        yield finalans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 5 4 2 3
