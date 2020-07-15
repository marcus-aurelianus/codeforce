import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,s = list(map(int,input().split()))
        *a, = list(map(int,input().split()))
        res = 0
        ma = 0
        max_ind = 1
        for i in range(n):
            cur = a[i]
            if cur > ma:
                ma = cur
                max_ind = i + 1
            if res + cur > s:
                yield max_ind
                break
            res += cur
        else:
            yield 0
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
