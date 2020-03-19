import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        lst = list(map(int,input().split()))
        odd=False
        even=False
        ans=True
        for ele in lst:
            if ele%2==0:
                even=True
                if odd:
                    ans=False
                    break
            else:
                odd=True
                if even:
                    ans=False
                    break
        if ans:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
