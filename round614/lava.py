import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
blocked={}
lavablock={}
def lava():
    for _ in range(q):
        r,c = [int(x) for x in input().split()]
        getlava=blocked.get((r,c),False)
        getlavablocks=lavablock.get((r,c),False)
        if getlava:
            del blocked[(r,c)]
            if getlavablocks:
                del lavablock[(r,c)]            
        else:
            blocked[(r,c)]=True
        #print(blocked)
        if not lavablock:
            for lav in blocked:
                posx,posy=lav
                if posx==1:
                    newposx=2
                else:
                    newposx=1
                lavprev=blocked.get((newposx,posy-1),False)
                lavcur=blocked.get((newposx,posy),False)
                lavnext=blocked.get((newposx,posy+1),False)
                if lavprev:

                    lavablock[(newposx,posy-1)]=True
                    break
                elif lavcur:

                    lavablock[(newposx,posy)]=True
                    break
                elif lavnext:

                    lavablock[(newposx,posy+1)]=True
                    break
        if lavablock:
            yield "No"
        else:
            yield "Yes"

        #print(blocked,lavablock)


if __name__ == '__main__':
    t,q= [int(x) for x in input().split()]
    ans = lava()
    print(*ans,sep='\n')
