import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t): 

        n, a,b,da,db = list(map(int,input().split()))
        dic = defaultdict(lambda:[])
        for i in range(n-1):
            s,e = list(map(int,input().split()))
            dic[s].append(e)
            dic[e].append(s)
##            
##        canfind = False
##        bfs = [a]
##        traversedTF = defaultdict(lambda:False)
##        while bfs:
##            newbfs = []
##            for ele in bfs:
##                if ele == b:
##                    canfind = True
##                
##                traversedTF[ele] = True
##                for ding in dic[ele]:
##                    if not traversedTF[ding]:
##                        newbfs.append(ding)
##            bfs = newbfs
        if not canfind:
            yield 'Bob'
        else:
            traversed = defaultdict(lambda:False)
            bfs=[]
            for ele in dic:
                if len(dic[ele])==1: #and traversedTF[ele]:
                    bfs.append(ele)
            maxi = -1
            while bfs:
                newbfs = []
                for ele in bfs:
                    traversed[ele] = True
                    for ding in dic[ele]:
                        if not traversed[ding]:
                            newbfs.append(ding)
                bfs = newbfs
                maxi += 1
            if da>=maxi or da>=db:
                yield 'Alice'
            else:
                yield 'Bob'
                    
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
