import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import deque
def gift():
    for _ in range(t):
        n=int(input())

        arry=input()
        
        zstk=deque()
        ostk=deque()
        
        ans=[0]*n
        len0,len1=0,0
        if arry[0]=='1':
            ostk.append(1)
            len1+=1
        else:
            zstk.append(1)
            len0+=1
        ans[0]=1
        curr=1
        for i in range(1,n):
            if arry[i]=='1':
                if len0==0:
                    curr+=1
                    len1+=1
                    ostk.append(curr)
                    ans[i]=curr
                else:
                    ele=zstk.popleft()
                    len0-=1
                    len1+=1
                    ostk.append(ele)
                    ans[i]=ele
            else:
                if len1==0:
                    curr+=1
                    len0+=1
                    zstk.append(curr)
                    ans[i]=curr
                else:
                    ele=ostk.popleft()
                    len1-=1
                    len0+=1
                    zstk.append(ele)
                    ans[i]=ele
        yield curr
        yield " ".join(str(x) for x in ans)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 5 4 2 3
