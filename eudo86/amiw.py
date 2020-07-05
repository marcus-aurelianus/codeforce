import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        kap=input()
        count0,count1=kap.count('0'),kap.count('1')
        diulei=int(kap,2)
        if count0==0 or count1==0:
            yield kap
        else:
            if kap[0]=='0':
                startpattern='01'
            else:
                startpattern='10'
            n=len(kap)
            i=1
            mul=1
            while i<n:
                tis=kap[i]
                prev=kap[i-1]
                if tis==kap[0]:
                    mul+=1
                else:
                    if prev!=kap[0]:
                        mul+=1
                i+=1
            yield startpattern*mul
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
