import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string=input()

        n=len(string)
        ans=float("inf")
        res=[]
        tisround=1
        for i in range(n):
            curr=string[i]
            if i!=n-1:
                next1=string[i+1]
                if curr==next1:
                    tisround+=1
                else:
                    res.append(tisround)
                    tisround=1
            else:
                res.append(tisround)
        m=len(res)
        if m==1:
            yield 0
        else:
            for i in range(m-1):
                tempans=0
                if i%2:
                    #print(i,m,res)
                    for j in range(i):
                        if j%2==0:
                            tempans+=res[j]
                    for j in range(i+1,m):
                        if j%2:
                            tempans+=res[j]
                else:
                    for j in range(i):
                        if j%2:
                            tempans+=res[j]
                    for j in range(i+1,m):
                        if j%2==0:
                            tempans+=res[j]
                ans=min(ans,tempans)        
            yield ans
                    
            


             
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
