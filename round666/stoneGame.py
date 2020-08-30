import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

            
def gift():
    for _ in range(t):
        n = input()
        arry = list(map(int,input().split()))
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


#1 3 2 4
#1 12 8 12
#4 
