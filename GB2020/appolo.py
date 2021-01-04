import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

mod = 10**9+7
def gift():
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        sumCurr = 0
        ans = 0
        for i in range(n):
            prevSum = sumCurr
            sumCurr += lst[i]
            if lst[i]:
                ans= (ans + lst[i]*sumCurr*n)%mod
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
