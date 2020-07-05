
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        maps=[]
        for i in range(n):
            kap=list(input())
            maps.append(kap)
        ans=True
        for i in range(n):
            for j in range(n):
                if maps[i][j]=='1':
                    if i!=n-1 and j!=n-1:
                        if maps[i+1][j]!='1' and maps[i][j+1]!='1':
                            ans=False
                            break
        if ans:
            yield 'YES'
        else:
            yield 'NO'
 

        
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
