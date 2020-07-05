import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

inamo='qwertyuiopasdfghjklzxcvbnm'
#print(len(inamo))
def gift():
    for _ in range(t):
        n,a,b = list(map(int,input().split()))
        kap=inamo[:b]

        yield kap*(n//b)+kap[:n%b]
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
