import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,n,m= list(map(int,input().split()))
        for i in range(n):
            pcdbm=x-(x//2+10)
            if pcdbm>0:
                x-=pcdbm
            else:
                break
            #print(x)
        #print(x)
        if x>10*m:
            yield 'NO'
        else:
            yield 'YES'



if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
