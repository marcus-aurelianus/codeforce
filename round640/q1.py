import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        kap=int(input())
        res=[]
        while kap!=0:
            lenk=len(str(kap))
            dd=kap//(10**(lenk-1))
            res.append(10**(lenk-1)*dd)
            kap=kap%(10**(lenk-1))
        yield(len(res))
        yield " ".join(str(x) for x  in res)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
