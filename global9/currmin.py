import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))

        


        currmin=arry[0]
        foundless=False
        for i in range(1,n):
            
            curr=arry[i]
            
            prev=arry[i-1]
            if curr<=currmin:
                if not foundless:
                    foundless=True


            if prev<curr:
                if foundless:
                    if curr>currmin:
                        foundless=False
                


        if not foundless:
            yield 'YES'
        else:
            yield 'NO'


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
