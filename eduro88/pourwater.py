import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        h,c,tem = list(map(int,input().split()))


        if h==tem:
            yield 1
        elif (h+c)/2>tem:
            mid=(h+c)/2

            edif=abs(h-c)
            ldif=abs(mid-c)
            if edif>=ldif:
                yield 2
            else:
                yield 1
        elif (h+c)/2==tem:
            yield 2
        else:
            
            dif= tem-(h+c)/2
            posans=((h-c)/2)//dif
            bibi=((h-c)/2)%dif

            if posans%2==0:
                posans+=1
            oposans=posans+2
            pdif=abs(tem-((h+c)/2+(h-c)/2/posans))
            edif=abs(tem-((h+c)/2+(h-c)/2/oposans))
            if oposans>=3:
                
                kposans=posans-2
                kdif=abs(tem-((h+c)/2+(h-c)/2/kposans))
                mindif=min(pdif,edif,kdif)
                if mindif==pdif:
                    yield int(posans)
                elif mindif==edif:
                    yield int(oposans)
                else:
                    yield int(kposans)
            else:
            
            #print(pdif,edif,posans,oposans)
                if pdif<edif:
                    yield int(posans)
                else:
                    yield int(oposans)


                        
            
        

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
