import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

blocks={}

lavablocks={}
def newlava():
    for _ in range(q):
        r,c = [int(x) for x in input().split()]
        getlavablocks=blocks.get((r,c),False)
        if r==1:
            newposx=2
        else:
            newposx=1
        lavprev=blocks.get((newposx,c-1),False)
        lavcur=blocks.get((newposx,c),False)
        lavnext=blocks.get((newposx,c+1),False)
        if getlavablocks:
            del blocks[(r,c)]
            freq=lavablocks.get((newposx,c-1),0)
            if freq:
                if freq==1:
                    del lavablocks[(newposx,c-1)]
                else:
                    lavablocks[(newposx,c-1)]=freq-1
                freq=lavablocks.get((r,c),0)
                if freq:    
                    if freq==1:
                        del lavablocks[(r,c)]
                    else:
                        lavablocks[(r,c)]=freq-1
            
            freq=lavablocks.get((newposx,c),0)
            if freq:
                if freq==1:
                    del lavablocks[(newposx,c)]
                else:
                    lavablocks[(newposx,c)]=freq-1
                freq=lavablocks.get((r,c),0)
                if freq:    
                    if freq==1:
                        del lavablocks[(r,c)]
                    else:
                        lavablocks[(r,c)]=freq-1
            freq=lavablocks.get((newposx,c+1),0)
            if freq:
                if freq==1:
                    del lavablocks[(newposx,c+1)]
                else:
                    lavablocks[(newposx,c+1)]=freq-1
                freq=lavablocks.get((r,c),0)
                if freq:    
                    if freq==1:
                        del lavablocks[(r,c)]
                    else:
                        lavablocks[(r,c)]=freq-1
        else:
            blocks[(r,c)]=True
            
            if lavprev:
                freq=lavablocks.get((newposx,c-1),0)
                lavablocks[(newposx,c-1)]=freq+1
                freq=lavablocks.get((r,c),0)
                lavablocks[(r,c)]=freq+1
            if lavcur:
                freq=lavablocks.get((newposx,c),0)
                lavablocks[(newposx,c)]=freq+1
                freq=lavablocks.get((r,c),0)
                lavablocks[(r,c)]=freq+1
            if lavnext:
                freq=lavablocks.get((newposx,c+1),0)
                lavablocks[(newposx,c+1)]=freq+1
                freq=lavablocks.get((r,c),0)
                lavablocks[(r,c)]=freq+1
        #print(len(lavablocks)) 

        if lavablocks:
            yield 'No'
        else:
            yield 'Yes'
        #print(blocks,lavablocks)
            
if __name__ == '__main__':
    t,q= [int(x) for x in input().split()]
    ans = newlava()
    print(*ans,sep='\n')
