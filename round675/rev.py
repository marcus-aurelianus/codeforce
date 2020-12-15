import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        array = []
        for i in range(n):
            eachRow = list(map(int,input().split()))
            array.append(eachRow)

        rows = n//2 + n%2
        cols = m//2 + m%2
        ans = 0
        for i in range(rows):
            for j in range(cols):
                #print(i,j,ans)
                #print(i,j,n,i==rows-1 and i==n//2,j==cols-1 and j==m//2)
                if i==n//2:
                    #print('t')
                    if j==m//2:
                        continue
                    else:
                        f, nex = array[i][j],array[i][m-1-j]
                        diu = (f+nex)//2
                        diu1 = diu+1
                        dium1 = diu-1
                        ans += min((abs(f-diu)+abs(nex-diu)),(abs(f-diu1)+abs(nex-diu1)),(abs(f-dium1)+abs(nex-dium1)))
                else:
                    if j==m//2:
                        f, nex = array[i][j],array[n-1-i][j]
                        diu = (f+nex)//2
                        diu1 = diu+1
                        dium1 = diu-1
                        ans += min((abs(f-diu)+abs(nex-diu)),(abs(f-diu1)+abs(nex-diu1)),(abs(f-dium1)+abs(nex-dium1)))
                    else:
                        a,b,c,d = array[i][j],array[n-1-i][j],array[i][m-1-j],array[n-1-i][m-1-j]
                        diuArray = [a,b,c,d]
                        diuArray.sort()
                        diu = (diuArray[1]+diuArray[2])//2
                        diu1 = diu+1
                        num1 = abs(a-diu)+abs(b-diu)+abs(c-diu)+abs(d-diu)
                        num2 = abs(a-diu1)+abs(b-diu1)+abs(c-diu1)+abs(d-diu1)
                        ans += min(num1,num2)
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)



# 1 x 1 x 1
# 1 1 1 1 1
# y 1 1 1 y
# 1 1 1 1 1
# 1 x 1 x 1







