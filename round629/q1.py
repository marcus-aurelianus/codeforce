import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        c=a%b
        if c==0:
            yield 0
        else:
            yield b-c

     
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
