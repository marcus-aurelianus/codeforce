import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
def gift():
    for _ in range(1):
        n,x=list(map(int,input().split()))
        days=list(map(int,input().split()))
        diulei=max(days)
        if diulei>=x:
            #print(x+x-diulei)
            yield (diulei+diulei-x+1)*(x)//2
        else:
            posans=[]
            for pos1 in range(n):
                curpos=pos1
                front,back=[days[pos1]],[days[pos1]]
                fres,bres=days[pos1],days[pos1]
                while True:
                    curpos=(curpos+1)%(n)
                    front.append(days[curpos])
                    fres+=days[curpos]
                    if fres>=x:
                        break
                posans.append(front)
                curpos=pos1
                while True:
                    curpos=(curpos-1)%(n)
                    #print(curpos)
                    back.append(days[curpos])
                    bres+=days[curpos]
                    if bres>=x:
                        break
                posans.append(back)
            posans.sort(reverse=True)
            maxans=0
            for posinamo in posans:
                ans=0
                xtemp=x
                for pp in posinamo:
                    if xtemp>pp:
                        ans+=(pp+1)*(pp)//2
                        xtemp-=pp
                    else:
                        ans+=(pp+pp-xtemp+1)*(xtemp)//2
                        break
                maxans=max(ans,maxans)
            yield maxans
                    
                    
        
if __name__ == '__main__':
    ans = gift()
    print(*ans,sep='\n')
            



1,2,3,4,1,1,1,2,3,1,2,3,1
