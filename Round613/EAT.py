def mssl(l):
    best = cur = 0
    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best
def cake():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        sum1, best1,best2 = sum(a), mssl(a[1:]),mssl(a[:-1])
        if sum1>best1 and sum1>best2:
            yield 'YES'
        else:
            yield 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = cake()
    print(*ans,sep='\n')
