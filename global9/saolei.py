import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def iscorner(p1,p2,n,m):
    if p1 ==0:
        if p2==m-1 or p2==0:
            return True
        else:
            return False
    elif p1==n-1:
        if p2==m-1 or p2==0:
            return True
        else:
            return False
    else:
        return False
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        arry=[]
        for i in range(n):
            temp = list(map(int,input().split()))
            arry.append(temp)
        geit=True 
        for i in range(n):
            if not geit:
                break
            for j in range(m):
                if iscorner(i,j,n,m):
                    if arry[i][j]>2:
                        geit=False
                        break
                    else:
                        arry[i][j]=2
                elif i==0 or i==n-1 or j==0 or j==m-1:
                    if arry[i][j]>3:
                        geit=False
                        break
                    else:
                        arry[i][j]=3
                else:
                    if arry[i][j]>4:
                        geit=False
                        break
                    else:
                        arry[i][j]=4
        if geit:
            yield 'YES'
            for i in range(n):
                yield " ".join(str(x) for x in arry[i])
        else:
            yield 'NO'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
