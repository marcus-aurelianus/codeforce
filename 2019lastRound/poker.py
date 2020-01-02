def poker():
    for _ in range(t):
        n,k1,k2 = [int(x) for x in input().split()]
        *a, = [int(x) for x in input().split()]
        *b, = [int(x) for x in input().split()]
        if max(a)>max(b):
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = poker()
    print(*ans,sep='\n')
