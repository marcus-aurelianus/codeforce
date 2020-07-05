import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry=list(map(int,input().split()))
        arry.sort()
        ans=[]
        if n%2:
            ans.append(arry[n//2])
        for i in range(n//2):
            if n%2:
                ans.append(arry[n//2-i-1])
                ans.append(arry[n//2+i+1])
            else:
                ans.append(arry[n//2-i-1])
                ans.append(arry[n//2+i])

        yield " ".join(str(x) for x in ans)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
