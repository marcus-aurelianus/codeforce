import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry=list(map(int,input().split()))
        maxlen=1
        maxnum=arry[0]
        res=0
        if n==1:
            yield arry[0]
        else:
            for i in range(1,n):
                curr=arry[i-1]
                nex1=arry[i]
                if (curr>0 and nex1<0) or (curr<0 and nex1>0) :
                    maxlen+=1
                    res+=maxnum
                    maxnum=arry[i]
                else:
                    maxnum=max(maxnum,arry[i])
                if i==n-1:
                    res+=maxnum
            yield res
             
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
 
