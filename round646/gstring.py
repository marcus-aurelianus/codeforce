import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string=input()
        s=string[0]
        n=len(string)
        ans=0
        revans=0
        containoppo=False
        revcontainoppo=False
        opps=0
        revopps=0

        revs=string[n-1]


        for i in range(n-1):
            curr=string[i+1]
            revcurr=string[n-2-i]
            if curr!=s:
                containoppo=True
                if i!=n-2:
                    opps+=1
            if containoppo:
                if curr==s:
                    ans+=1

            if revcurr!=revs:
                revcontainoppo=True
                if i!=n-2:
                    revopps+=1
            if revcontainoppo:
                if revcurr==revs:
                    revans+=1

            
        yield min(ans,opps,revans,revopps)
             
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
