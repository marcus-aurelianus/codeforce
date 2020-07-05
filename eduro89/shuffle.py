import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,x,m = list(map(int,input().split()))
        se=[x,x]
        for i in range(m):
            s,e=  list(map(int,input().split()))
            prevs,preve=se

            news,newe=prevs,preve

            #print(preve,prevs,e,s)
            if not (preve<s or prevs>e):
                news=min(prevs,s)
                newe=max(preve,e)
            se=[news,newe]
            #print(se)
        yield se[1]-se[0]+1


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


# 2x+y<a
# 2y+x<b

#3x+3y<a+b
#x<
            
