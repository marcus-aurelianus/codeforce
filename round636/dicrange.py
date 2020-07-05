import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(t):
        n,k=list(map(int,input().split()))
        arry=list(map(int,input().split()))
        dic={}
        ragngerino=[2,k*2]
        for i in range(n//2):
            sumtis=arry[i]+arry[n-1-i]
            freq=dic.get(sumtis,0)
            dic[sumtis]=freq+1
            minnum=1+min(arry[i],arry[n-1-i])
            maxnum=k+max(arry[i],arry[n-1-i])
            a,b=ragngerino
            a=max(minnum,a)
            b=min(maxnum,b)
            ragngerino=[a,b]
            #print(ragngerino)
        ans=n//2

        for ele in dic:
            s,e=ragngerino
            if s<=ele<=e:
                ans=min(ans,n//2-dic[ele])
            else:
                counter=0
                for i in range(n//2):
                    if arry[i]+arry[n-1-i]==ele:
                        continue
                    minnum=1+min(arry[i],arry[n-1-i])
                    maxnum=k+max(arry[i],arry[n-1-i])
                    if minnum<=ele<=maxnum:
                        counter+=1
                    else:
                        counter+=2
                ans=min(ans,counter)

        
        yield ans
             
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
 
