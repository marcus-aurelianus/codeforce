def minutes():
    for _ in range(n):
        *a, = [int(x) for x in input().split()]
        yield 60*(23-a[0])+(60-a[1])
if __name__ == '__main__':
    n= int(input())
    ans = minutes()
    print(*ans,sep='\n')
