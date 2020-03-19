import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        neck = [int(x) for x in input().split()]
        brace = [int(x) for x in input().split()]
        neck.sort()
        brace.sort()
        yield " ".join(str(x) for  x in neck)
        yield " ".join(str(x) for  x in brace)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
