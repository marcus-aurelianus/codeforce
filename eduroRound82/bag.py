import sys
import math

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def fillbag():
    for _ in range(t):
        n,m=map(int,input().split())
        baglogs=list(map(int,input().split()))
        baglogs.sort(reverse=True)
        tempn=n
        currpos=0
        res=0
        found=True
        while tempn>0:
            k=int(math.log(n, 2))
            tempnum=2**k
            if tempnum<=baglogs[currpos]:
                res+=(math.log(baglogs[0],2)-k)
                tempn-=tempnum
                currpos+=1
                continue
            else:
                if tempn==sum(baglogs[currpos:]):
                    break
                else:
                    found=False
                    break
        if found:
            yield res
        else:
            yield -1

        

        
if __name__ == '__main__':
    t= int(input())
    ans = fillbag()
    print(*ans,sep='\n')
            
