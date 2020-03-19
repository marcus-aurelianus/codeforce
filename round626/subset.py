import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        odd=[]
        found=False
        for i in range(n):
            if array[i]%2==0:
                yield(1)
                yield(i+1)
                found=True
                break
            else:
                odd.append(i+1)
                if len(odd)==2:
                    yield(2)
                    yield(" ".join(str(x) for  x in odd))
                    found=True
                    break
                else:
                    continue
        if not found:
            yield(-1)
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
