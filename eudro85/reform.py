import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,x=list(map(int,input().split()))

        wealth= list(map(int,input().split()))
        sum1=0
        counter=0
        wealth.sort()
        for i in range(n):
            ele=wealth[i]
            if ele>=x:
                sum1+=(ele-x)
                counter+=1

        for i in range(n):
            ele=wealth[n-i-1]
            if ele<x:
                kap=x-ele
                if sum1>=kap:
                    sum1-=kap
                    counter+=1
                else:
                    break
        yield counter
        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
