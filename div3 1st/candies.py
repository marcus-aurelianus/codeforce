def minutes():
    for _ in range(t):
        n,k = [int(x) for x in input().split()]
        remainder = n%k
        maxRemain=k//2
        res=n//k
        if remainder==0:
            yield n
        elif maxRemain>=remainder:
            yield n
        else:
            yield k*res+maxRemain
if __name__ == '__main__':
    t= int(input())
    ans = minutes()
    print(*ans,sep='\n')
