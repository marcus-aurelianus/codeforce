import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        ina=int(input())
        lst = list(map(int,input().split()))
        ansp=[lst[0]]+[None]*(ina-1)
        ansb=[None]*(ina-1)+[lst[ina-1]]

        dic1={lst[0]:1}
        dic2={}
        for i in range(1,ina):
            front=lst[i]
            back=lst[ina-i-1]
            currmaxf=ansp[i-1]
            currmaxb=ansb[ina-i]
            ansp[i]=max(front,currmaxf)
            ansb[ina-i-1]=max(back,currmaxb)

            freq=dic2.get(lst[i],0)
            dic2[lst[i]]=freq+1
        #print(ansp,ansb)
        #print(dic1,dic2)
        len1,len2=len(dic1),len(dic2)
        ans=[]
        if ansp[0]==1 and ansb[1]==len2 and ansb[1]==ina-1:
            #print('kappa',lst)
            ans.append([1,ina-1])
        for i in range(1,ina-1):
            front=ansp[i]
            back=ansb[i+1]
            ele=lst[i]

            freq1=dic1.get(ele)
            if freq1:
                break
            else:
                len1+=1
                dic1[ele]=1
            freq2=dic2.get(ele)
            dic2[ele]=freq2-1
            #print(ele,dic1,dic2,len1,len2,front,back)
            if freq2==1:
                len2-=1
            if front==i+1 and back==ina-i-1 and front==len1 and back==len2:
                ans.append([i+1,ina-(i+1)])
        yield len(ans)
        for kap in ans:
            yield str(kap[0])+" "+str(kap[1])

            
                
                    
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
