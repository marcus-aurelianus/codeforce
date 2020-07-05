import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k=map(int,input().split())
        if n<k:
            yield 'NO'
        else:
            if n%2==0:
                if n>=k*2:
                    ans=[2]*(k-1)+[n-2*(k-1)]
                    yield 'YES'
                    yield " ".join(str(x) for x in ans)
                else:
                    dd=(3*k-n)//2
                    dl=(3*k-n)/2
                    if dd==dl:
                        ans=[1]*(dd)+[3]*(k-dd)
                        yield 'YES'
                        yield " ".join(str(x) for x in ans)
                    else:
                        yield 'NO'
            else:
                if n>=k and k%2:
                    yield 'YES'
                    ans=[1]*(k-1)+[n-(k-1)]
                    yield " ".join(str(x) for x in ans)
                else:
                    yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')



##100 55
##1 3 5
##33  22

##x+3*(k-x)=n
##n=3*k-2*x
##x=(3*k-n)//2
##1 3 1 3 1 3 49
            
