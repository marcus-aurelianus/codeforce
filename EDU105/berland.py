import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,*dirs = list(map(int,input().split()))
        ans = True

        for i,d in enumerate(dirs):
            if d==n-1:
                if dirs[(i+1)%4]+dirs[(i+3)%4]==0:
                    ans = False
                    break
            elif d==n:
                if dirs[(i+1)%4]==0 or dirs[(i+3)%4]==0:
                    ans = False
            if d==n and dirs[(i+2)%4]==n:
                if dirs[(i+1)%4]<2 or dirs[(i+3)%4]<2:
                    ans = False
            elif d == n and dirs[(i+2)%4]==n-1:
                if dirs[(i+1)%4]+dirs[(i+3)%4]<3:
                    ans = False
            elif d == n-1 and dirs[(i+2)%4]==n-1:
                if dirs[(i+1)%4]+dirs[(i+3)%4]<2:
                    ans = False
        yield 'YES' if ans else 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
