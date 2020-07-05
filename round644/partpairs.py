import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        arry.sort()
        mindiff=float("inf")
        even,odd=0,0
        for i in range(n):
            if arry[i]%2:
                odd+=1
            else:
                even+=1
        if odd%2==0:
            yield 'YES'
        else:
            found=False
            for i in range(n-1):
                if abs(arry[i]-arry[i+1])==1:
                    found=True
                    break
            if found:
                yield 'YES'
            else:
                yield 'NO'
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
