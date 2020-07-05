import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,n = list(map(int,input().split()))
        c,d=min(a,b),max(a,b)

        counter=0
        while max(c,d)<=n:
            e,f=min(c,d),max(c,d)
            c,d=e+f,f
            counter+=1
        yield counter
         
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


# a b
# a a+b
# 2a+b a+b
# 2a+b 3a+2b
# 5a+3b 3a+2b
# 5a+3b 8a+5b
# 13a+8b 7a+5b
# 11a+8b 18a+13b
            

