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

        ans=[]
        checkdiff=True
        for i in range(n):
            for j in range(i,n):
                if checkdiff:
                    counter=0
                    for k in range(m):
                        if arrys[i][k]!=arrys[j][k]:
                            counter+=1
                        if counter>2:
                            checkdiff=False
                            break
                else:
                    break
        if checkdiff:
            for j in range(m):

                counterdic={}
                for i in range(n):
                    ele=arrys[i][j]
                    freq=counterdic.get(ele,0)
                    counterdic[ele]=freq+1
                #print(counterdic,len(counterdic),arrys[0][j])
                if len(counterdic)==1:
                    ans.append(arrys[0][j])
                else:
                    ans.append(list(counterdic.keys()))
            pans=ans[0]
            for  j in range(1,m):
                #print(pans,ans)
                tis=ans[j]
                #print(tis,pans,ans)
                tans=[]
                if len(tis)==1:
                    
                    for di in pans:
                        di+=tis
                        tans.append(di)
                else:
                    for di in pans:
                        for ti in tis:
                            diu=di+ti
                            tans.append(diu)
                    #print(tans)
                pans=tans
            gotans=False       
            for ina in pans:
                ans=True
                for i in range(n):
                    counter=0
                    for j in range(m):
                        #print(arrys)
                        if ina[j]!=arrys[i][j]:
                            counter+=1
                        if counter>=2:
                            ans=False
                            break
                if ans:
                    yield ina
                    gotans=True
                    break
            if not gotans:
                yield -1
        else:
            yield -1
    
#aaaab
#abaaa
#aaaab
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
