import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        arrys=[]
        for i in range(n):
            kap=list(input())
            arrys.append(kap)
        diffdic={}
        for i in range(n):
            for j in range(m):
                for k in range(i+1,n):
                    if arrys[i][j]!=arrys[k][j]:
                        kap=diffdic.get(j,[])
                        kap.append([i,k])
                        diffdic[j]=kap
        if len(diffdic)>2:
            yield -1
        else:
            ans=""
            notin=[]
            for j in range(m):
                if j not in diffdic:
                    ans+=arrys[0][j]
                else:
                    counterdic={}
                    for i in range(n):
                        ele=arrys[i][j]
                        freq=counterdic.get(ele,0)
                        counterdi[ele]=freq+1
                    maxele=max(counterdic, key=counterdic.get)
                    
        yield diffdic
#aaaab
#abaaa
#aabbb
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
