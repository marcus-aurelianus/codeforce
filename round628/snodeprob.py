import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n=int(input())
dic={}
seq={}
for i in range(n-1):
    u,v=list(map(int,input().split()))
    ulist=dic.get(u,[])
    vlist=dic.get(v,[])
    ulist.append(v)
    vlist.append(u)
    dic[u]=ulist
    dic[v]=vlist
    seq[(u,v)]=i

ans=[-1]*(n-1)

curr=0

for lis in dic:
    nodes=dic[lis]
    if len(nodes)==1:
        #print(seq,(lis,dic[lis][0]))
        seqloc=seq.get((lis,dic[lis][0]),False)
        seqloc1=seq.get((dic[lis][0],lis),False)
        if seqloc:
            ans[seqloc]=curr
            curr+=1
        elif seqloc1:
            ans[seqloc1]=curr
            curr+=1
            
for i in range(n-1):
    if ans[i]==-1:
        ans[i]=curr
        curr+=1
for an in ans:
    print(an)
    
