import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,s = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        diu=sum(arry)
        if diu%s:
            yield n
        else:
            frontc=0
            backc=0
            f,b=True,True
            for i in range(n):
                #print(ans)
                front=arry[i]
                back=arry[n-1-i]
                if f:
                    frontc+=1
                if front%s:
                    f=False
                if b:
                    backc+=1
                if back%s:
                    b=False  

          
            diulei=n-min(frontc,backc)
            if diulei:
                yield diulei
            else:
                yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
