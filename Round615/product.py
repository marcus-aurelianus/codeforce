import sys
from functools import reduce
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

def product():
    for _ in range(t):
        n=int(input())
        yn=factors(n)
        yn.sort()
        #print(yn)
        if len(yn)>=4:
            a,b=yn[1],yn[3]
            c=n//yn[1]//yn[3]
            d=n//yn[1]%yn[3]

            a1,b1=yn[1],yn[2]
            e=n//yn[1]//yn[2]
            f=n//yn[1]%yn[2]
            if c>1 and c!=a and c!=b and d==0:
                yield 'YES'
                yield str(a)+' '+str(b)+' '+str(c)
            elif e>1 and e!=a1 and e!=b1 and f==0:
                yield 'YES'
                yield str(a1)+' '+str(b1)+' '+str(e)
            else:
                yield'NO'
        else:
            yield 'NO'


if __name__ == '__main__':
    t= int(input())
    ans = product()
    print(*ans,sep='\n')
