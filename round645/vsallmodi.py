import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def dude(pp):
    return (pp+1)*(pp)//2
def gift():
    for _ in range(1):
        n,x=list(map(int,input().split()))
        days=list(map(int,input().split()))
        diulei=max(days)
        if diulei>=x:
            #print(x+x-diulei)
            yield (diulei+diulei-x+1)*(x)//2
        else:
            s,e=0,0
            maxans=0

            front=[]
            fres=0

            curans=0
            tored=0
            while s<=n-1:
                
                if s>=1:
                    fres-=days[s-1]
                    curans-=dude(days[s-1])
                    curans-=tored
                #print(curans,maxans,fres,tored)
                while True:
                    #print('in',curans,maxans,fres,s,e,front)
                    if fres>=x:
                        #print('checkfres',fres)

                        fres-=days[(e-1)%n]
                        #print('checkfres',fres)
                        e=(e-1)%(n)
                        break
                    
                    front.append(days[e])
                    fres+=days[e]
                    
                    if fres<=x:
                        curans+=dude(days[e])
                        if fres==x:
                            tored=dude(days[e])
                    else:
                        #print('xtempround')
                        pp=days[e]
                        xtemp=x-(fres-pp)
                        curans+=(pp+pp-xtemp+1)*(xtemp)//2
                        tored=(pp+pp-xtemp+1)*(xtemp)//2
                    e=(e+1)%(n)
                maxans=max(curans,maxans)
                s+=1
            yield maxans

                    
                    
        
if __name__ == '__main__':
    ans = gift()
    print(*ans,sep='\n')
            



1,2,3,4,1,1,1,2,3,1,2,3,1
