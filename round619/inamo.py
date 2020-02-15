import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def dogshit():
    for _ in range(t):
        n,m=map(int,input().split())
        o=n-m
        stdo=o//(m+1)
        stdol=o%(m+1)
        #print(stdo,stdol,m)
        #print(n*(n+1)/2,stdo*(stdo+1)//2*(m-stdol),(stdo+stdo+1)*(stdo+stdo+2)//2*(stdol))
        res=n*(n+1)//2-stdo*(stdo+1)//2*(m+1-stdol)-(stdo+1)*(stdo+2)//2*(stdol)
        yield res
                        
if __name__ == '__main__':
    t= int(input())
    ans = dogshit()
    print(*ans,sep='\n')
            
