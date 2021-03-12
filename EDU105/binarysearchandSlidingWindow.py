import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import bisect
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        boxs = list(map(int,input().split()))
        poss = list(map(int,input().split()))
        ans = 0 
        if boxs[0]<0 and poss[0]<0:
            sb = bisect.bisect_left(boxs,0)
            sp = bisect.bisect_left(boxs,poss[0])
            print(sb,sp)
            ans = max(sb-sp,ans)
        if boxs[-1]>0 and poss[-1]>0:
            eb = bisect.bisect_right(boxs,0)
            ep = bisect.bisect_right(boxs,poss[-1])
            print(eb,ep)
            ans = max(ep-eb,ans)
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
