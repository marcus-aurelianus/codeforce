import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

def gift():
    for _ in range(t):
        n=int(input())
        nums=list(map(int,input().split()))
        color=1
        ans=[1]

        for i in range(1,n):
            curr=nums[i]
            if i==n-1:
                next1=nums[0]
            else:
                next1=nums[i+1]
            if i==0:
                prev1=nums[n-1]
            else:
                prev1=nums[i-1]
            tempnum=ans[-1]
            if i!=n-1:
                if curr!=prev1 or curr!=next1:
                    ans.append((tempnum)%2+1)
                    color=2
                else:
                    ans.append(tempnum)
            else:
                tempina=ans[0]
                if tempina!=tempnum and curr!=prev1 and curr!=next1:
                    ans.append(3)
                    color=3
                else:
                    if tempina==tempnum:
                        if curr==prev1 and curr==next1:
                            ans.append(tempnum)
                        else:
                            ans.append((tempnum)%2+1)
                            color=2
                    else:
                        if curr==prev1:
                            ans.append(tempnum)
                        else:
                            ans.append(tempina)
                            
            
        yield color
        yield " ".join(str(x) for x in ans)
                
     
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
