import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,l,r = list(map(int,input().split()))
        start=1
        tmml=l
        for i in range(n):
            kap=(n-i-1)*2
            if tmml>kap:
                tmml-=kap
            else:
                start=i+1
        res=[]
        if tmml%2==0:
            res.append(start+(tmml//2))
        
        while True:
            for k in range(tmml//2,n-start):
                res.append(start)
                res.append(start+k)
                

        
#(n-1)*2
#(n-2)*2---x
#(n-x)*2
#((n-x)*2+(n-1)*2)*x/2=l
        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
