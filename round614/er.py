
def floor():
    for _ in range(t):
        n,s,k = [int(x) for x in input().split()]
        a = {int(x):True for x in input().split()}
        mindis=float('inf')
        for i in range(n):
            prevp=s-i
            nextp=s+i
            inornop=a.get(prevp,False)
            inornon=a.get(nextp,False)
            if prevp>0 and not inornop:
                yield i
                break
            elif nextp<=n and not inornon:
                yield i
                break
if __name__ == '__main__':
    t= int(input())
    ans = floor()
    print(*ans,sep='\n')
            
