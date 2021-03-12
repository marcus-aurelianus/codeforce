import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import bisect
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        boxs = list(map(int,input().split()))
        poss = list(map(int,input().split()))
        ap = []
        bp = []
        am = []
        bm = []
        for i in boxs:
            if i>0:
                ap.append(i)
            else:
                am.append(-1*i)
        for i in poss:
            if i>0:
                bp.append(i)
            else:
                bm.append(-1*i)
        am.reverse()
        bm.reverse()

        rembox = len(ap)
        setbox = 0
        pans = 0
        for i in range(len(bp)-1,-1,-1):
            nb = bp[i]
            while len(ap)>0 and ap[-1]>nb:
                rembox -= 1
                ap.pop()
            pans = max(pans, setbox + i - bisect.bisect_right(bp,nb-rembox) + 1)
            if len(ap)>0 and nb == ap[-1]:
                rembox -= 1
                setbox += 1
                ap.pop()

        mans = 0
        ap = am
        bp = bm
        rembox = len(ap)
        setbox = 0
        for i in range(len(bp)-1,-1,-1):
            
            nb = bp[i]
            while len(ap) > 0 and ap[-1] > nb:
                rembox -= 1
                ap.pop()
            
            mans = max(mans , setbox + i - bisect.bisect_right(bp,nb-rembox) + 1)
     
            if len(ap) > 0 and nb == ap[-1]:
                rembox -= 1
                setbox += 1
                ap.pop()             
        yield pans+mans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
