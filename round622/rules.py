import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,r1,r2 = [int(x) for x in input().split()]
        sum1=r1+r2
        
        if sum1<n:
            maxres=1
            minres=sum1-1
        elif sum1==n:
            maxres=1
            minres=n-1
        else:
            maxres=min(sum1-n+1,n)
            minres=n
        if sum1==3:
            if n<=2:
                yield "2 2"
            else:
                yield "1 2"
        elif sum1==2:
            yield "1 1"  
        else:
            yield str(maxres)+" "+str(minres)
        

                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

##1 4 
##2 5 
##5 1
##4 3
##3 1
##4 6
##3 7
##1 1
            
