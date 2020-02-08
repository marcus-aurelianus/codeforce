import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def oddsum():
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]

        counto,counte=False,False
        for i in range(n):
            if a[i]%2==0 and not counte:
                counte=True
            elif a[i]%2==1 and not counto:
                counto=True
            if counto and counte:
                break
        if counto and counte:
            yield "YES"
        else:
            if counto and n%2==1:
                yield "YES"
            else:
                yield "NO"
if __name__ == '__main__':
    t= int(input())
    ans = oddsum()
    print(*ans,sep='\n')
