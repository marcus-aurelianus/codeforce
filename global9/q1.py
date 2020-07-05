import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        ans=[]
        for i in range(n):
            if i%2:
                ans.append(-abs(arry[i]))
            else:
                ans.append(abs(arry[i]))
        yield " ".join(str(x) for x in ans)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
