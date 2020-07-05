import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from bisect import bisect_left
def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)

    return i

#print(find_lt([2,3],1))
def gift():
    for _ in range(t):
        n=int(input())
        ans=[None]*n
        blanks={n:[0]}
        sortdatlen={}
        for i in range(n):
            #print(blanks,ans)
            tofillkey=list(blanks.keys())[0]
            tofill=blanks[tofillkey]
##            sortorno=sortdatlen.get(tofillkey,False)
##            if not sortorno:
##                #print(tofill)
##                tofill.sort()
##                sortdatlen[tofillkey]=True
            l=tofill[0]
            r=tofill[0]+tofillkey-1
            #print(l,r)
            if r-l>=1:
                # even count of ele
                if (r-l+1)%2==0:
                    
                    mid=l+(r-l+1)//2-1
                    ans[mid]=i+1
                    rnewl,rnewr=[mid+1,r]
                    lengthr=rnewr-rnewl+1
                    didi=blanks.get(lengthr,[])

                    pos=bisect_left(didi, rnewl)

                    didi=didi[:pos]+[rnewl]+didi[pos:]

                    blanks[lengthr]=didi
                    #print(blanks)
                    if mid!=l:
                        lnewl,lnewr=[l,mid-1]
                        lengthl=lnewr-lnewl+1
                        didi=blanks.get(lengthl,[])
                        
                        pos=bisect_left(didi, lnewl)

                        didi=didi[:pos]+[lnewl]+didi[pos:]
                        blanks[lengthl]=didi
                    
                else:
                    mid=l+(r-l)//2
                    ans[mid]=i+1
                    lengthr=r-mid
                    lnewl,lnewr=[l,mid-1]
                    rnewl,rnewr=[mid+1,r]
                    didi=blanks.get(lengthr,[])
                    pos=bisect_left(didi, lnewl)

                    didi=didi[:pos]+[lnewl,rnewl]+didi[pos:]

                    blanks[lengthr]=didi
            else:
                ans[l]=i+1
            if len(tofill)==1:
               del blanks[tofillkey]
            else:
                tofill=tofill[1:]
                blanks[tofillkey]=tofill
        yield " ".join(str(x) for x in ans)
        


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
