import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry=list(map(int,input().split()))
        prev=arry[0]
        maxdis=0

        for i in range(1,n):
            if arry[i]<prev:
                maxdis=max(maxdis,abs(arry[i]-prev))
            else:
                prev=arry[i]
            #print(arry[i],prev)
        #print(maxdis)
        if maxdis:
            yield len(bin(maxdis)[2:])
        else:
            yield 0

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
