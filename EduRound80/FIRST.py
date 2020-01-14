import math
def optimize():
    for _ in range(t):
        n,d = [int(x) for x in input().split()]
        x = math.floor(((1+4*d)**0.5-0.5)/2)
        res=math.ceil(d/(x+1))+x
        if res<=n:
            yield('YES')
        else:
            yield('NO')

if __name__ == '__main__':
    t= int(input())
    ans = optimize()
    print(*ans,sep='\n')
