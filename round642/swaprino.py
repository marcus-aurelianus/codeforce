import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        lsta= list(map(int,input().split()))
        lstb= list(map(int,input().split()))
        lsta.sort()
        lstb.sort()
        res=sum(lsta)
        for i in range(k):
            if lsta[i]<lstb[n-i-1]:
                res+=(lstb[n-i-1]-lsta[i])
            else:
                break
        yield res


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
