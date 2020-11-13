import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))

        ans = []
        for i in range(n):
            ans.append(list(map(int,input().split())))
        dic = defaultdict(lambda:[])
        for i in range(n):
            for j in range(m):
                dic[ans[i][j]].append([i,j])

        dicKeys = sorted(dic.keys())
        changed = defaultdict(lambda:False)
        auxi = defaultdict(lambda:[])
        for key in dicKeys:
            item = dic[key]
            toadd = []
            for seq in item:
                i,j = seq
                adj = []
                if not changed[(i,j)]:
                    if i!=0 and [i-1,j] in dic[key] or [i-1,j] in auxi[key]:
                        adj.append(ans[i-1][j])
                    if j!=0 and [i,j-1]in dic[key] or [i,j-1] in auxi[key]:
                        adj.append(ans[i][j-1])
                    if i!=n-1 and [i+1,j] in dic[key] or [i+1,j] in auxi[key]:
                        adj.append(ans[i+1][j])
                    if j!=m-1 and [i,j+1] in dic[key] or [i,j+1] in auxi[key]:
                        adj.append(ans[i][j+1])
                    if ans[i][j]+1 in adj:
                        continue
                    if ans[i][j] in adj:
                        ans[i][j]+=1
                        changed[(i,j)]=True
                        toadd.append([i,j])
            for add in toadd:
                i, j = add
                if i!=0 and [i-1,j] in dic[key+1] and not changed[(i-1,j)]:
                     ans[i-1][j]+=1
                     auxi[key+2].append([i-1,j])
                     changed[(i-1,j)]=True
                if j!=0 and [i,j-1]in dic[key+1] and not changed[(i,j-1)]:
                     ans[i][j-1]+=1
                     auxi[key+2].append([i,j-1])
                     changed[(i,j-1)]=True
                if i!=n-1 and [i+1,j] in dic[key+1] and not changed[(i+1,j)]:
                     ans[i+1][j]+=1
                     auxi[key+2].append([i+1,j])
                     changed[(i+1,j)]=True
                if j!=m-1 and [i,j+1] in dic[key+1] and not changed[(i,j+1)]:
                     ans[i][j+1]+=1
                     auxi[key+2].append([i,j+1])
                     changed[(i,j+1)]=True
                auxi[key+1].append([i,j])
                
                    
        for i in range(n):
            yield " ".join([str(x) for x in ans[i]])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 1
# 2 3
# 2 2
