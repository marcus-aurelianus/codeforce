import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num=int(input())
        yield "1 "+str(num-1)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
