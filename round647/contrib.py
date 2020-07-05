import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,m = list(map(int,input().split()))
dic={}
for _ in range(m):
    a,b = list(map(int,input().split()))
    bibi=dic.get(a,[])
    bibi.append(b)

    cici=dic.get(b,[])
    cici.append(a)
    dic[a]=bibi
    dic[b]=cici

seq=list(map(int,input().split()))
ans=[]
dicseq={}
for i in range(n):
    bi=seq[i]
    curs=dicseq.get(bi,[])
    curs.append(i+1)
    dicseq[bi]=curs
keyrino=sorted(list(dicseq.keys()))

traversed={}
falserino=False
for key in keyrino:
    curr=[]
    firstime=dicseq[key]
    firstime.sort()
    if falserino:
        break
    for ele in firstime:
        currcounter=1
        diba=dic.get(ele)
        if diba:
            for aele in diba:
                aelerino=traversed.get(aele,False)
                if aelerino:
                    currcounter+=1
        if currcounter==key:
            ans.append(ele)
            traversed[ele]=True
        else:
            falserino=True
            break
if falserino:
    print(-1)
else:
    print(" ".join(str(x) for x in ans))


            
