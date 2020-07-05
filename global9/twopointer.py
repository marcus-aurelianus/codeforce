import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))

        s,e=0,n-1
        sofarmin=arry[s]
        prevmin=arry[s]
        currmin=arry[s]

        foundcurrmin=True
        ans=True
        for i in range(1,n):
            
            curr=arry[i]
            
            prev=arry[i-1]
            if prev<curr:
                if not foundcurrmin:
                    if curr>prevmin:
                        
                        currmin=curr
                        foundcurrmin=True
            else:
                if not foundcurrmin and curr<sofarmin:
                    ans=False
                    break
                foundcurrmin=False
                prevmin=currmin
                if curr>prevmin:
                    currmin=curr
                    foundcurrmin=True
            if i==n-1:
                if not foundcurrmin and curr<sofarmin:
                    ans=False
            sofarmin=min(sofarmin,prevmin)
 
        if ans:
            yield 'YES'
        else:
            yield 'NO'


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
