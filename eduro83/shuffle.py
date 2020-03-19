import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        array = list(map(int,input().split()))
        array.sort(reverse=True)
        yield " ".join(str(x) for x in array)
        



if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
