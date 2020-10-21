import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        grid=[]
        for i in range(n):
            tem = input()
            grid.append(tem)
        f1 = grid[0][1]
        f2 = grid[1][0]
        l1 = grid[n-1][n-2]
        l2 = grid[n-2][n-1]

        if f1 == f2:
            if l1==l2:
                if f1==l1:
                    yield 2
                    yield "1 2"
                    yield "2 1"
                else:
                    yield 0
            else:
                if f1==l1:
                    yield 1
                    yield "{} {}".format(n,n-1)
                else:
                    yield 1
                    yield "{} {}".format(n-1,n)
        else:
            if l1==l2:
                if f1==l1:
                    yield 1
                    yield "1 2"
                else:
                    yield 1
                    yield "2 1"
            else:
                if f1==l1:
                    yield 2
                    yield "1 2"
                    yield "{} {}".format(n-1,n)
                else:
                    yield 2
                    yield "1 2"
                    yield "{} {}".format(n,n-1)           

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 0 1 1 0
# 1 0 1 1
