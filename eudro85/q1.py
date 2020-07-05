import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        res=True
        pl,ps= list(map(int,input().split()))
        if pl<ps:
            res=False
        for i in range(1,n):
            cl,cs= list(map(int,input().split()))
            if cl<cs:
                res=False
            elif cl<pl or cs<ps:
                res=False
            incl,inlc=cl-pl,cs-ps
            if incl<inlc:
                res=False
            pl,ps=cl,cs
        
        if res:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
