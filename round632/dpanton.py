import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        lst1 = list(map(int,input().split()))
        lst2 = list(map(int,input().split()))
        p,m=False,False
        if lst1[0]!=lst2[0]:
            yield 'NO'
        else:
            if n==1:
                yield 'YES'
            for i in range(1,n):
                ele=lst1[i-1]
                if ele>0:
                    p=True
                elif ele<0:
                    m=True
                if lst2[i]>lst1[i] and not p:
                    yield 'NO'
                    break
                elif lst2[i]<lst1[i] and not m:
                    yield 'NO'
                    break
                if i==n-1:
                    yield 'YES'
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

