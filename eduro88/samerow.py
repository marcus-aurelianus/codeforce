import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m,x,y = list(map(int,input().split()))
        cost=0
        for i in range(n):
            diulei=input()
            s=0
            while s<=m-1:
                curele=diulei[s]
                if s<m-1:
                    nextele=diulei[s+1]
                    if curele=='.' and nextele=='.':
                        if y>=2*x:
                            cost+=(2*x)
                        else:
                            cost+=y
                        s+=1
                    elif curele=='.':
                        cost+=x
                else:
                    if curele=='.':
                        cost+=x
                s+=1
        yield cost

                        
            
        

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
