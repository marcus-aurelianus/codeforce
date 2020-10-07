import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,l = list(map(int,input().split()))
        flags = list(map(int,input().split()))

        s,e=0,n
        lSpeed,rSpeed = 1, 1
        timeSpend = 0
        lpos,rpos = 0, l
        while s<=e:
            if s==e:
                timeSpend+=(rpos-lpos)/(lSpeed+rSpeed)
                rpos=lpos
                break
            leftTime = (flags[s]-lpos)/lSpeed
            rightTime = (rpos-flags[e-1])/rSpeed

            if leftTime>rightTime:
                lpos +=  rightTime*lSpeed
                rpos -= rightTime*rSpeed
                rSpeed += 1
                timeSpend += rightTime
                e -= 1    
            elif leftTime<rightTime:
                lpos +=  leftTime*lSpeed
                rpos -= leftTime*rSpeed
                lSpeed += 1
                timeSpend += leftTime
                s+=1
            else:
                lpos +=  leftTime*lSpeed
                rpos -= leftTime*rSpeed
                lSpeed += 1
                rSpeed += 1
                timeSpend += leftTime
                s+=1
                e-=1
        #print(lpos,rpos)
        if lpos<rpos:
            timeSpend+=(rpos-lpos)/(lSpeed+rSpeed)
        yield timeSpend
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
