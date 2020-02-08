import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def cashback():
    for _ in range(t):
        n = int(input())
        cash=n
        rem=0
        res=0
        while cash>9:
            #print(cash)
            res+=(cash//10)
            cash=(cash//10+cash%10)
        yield res*10+cash
if __name__ == '__main__':
    t= int(input())
    ans = cashback()
    print(*ans,sep='\n')
