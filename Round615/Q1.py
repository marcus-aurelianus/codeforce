import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



def distribute():
    for _ in range(t):
        a,b,c,n = [int(x) for x in input().split()]
        if (a+b+c+n)%3==0 and max(a,b,c)*3-sum([a,b,c])<=n:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = distribute()
    print(*ans,sep='\n')
