import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string=input()
        n=len(string)
        maxdis=0
        prevR=0
        for i in range(n):
            if string[i]=='R':
                currdis=i+1-prevR
                maxdis=max(maxdis,currdis)
                prevR=i+1
            else:
                if i==n-1:
                    currdis=n+1-prevR
                    maxdis=max(maxdis,currdis)

        yield maxdis
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

