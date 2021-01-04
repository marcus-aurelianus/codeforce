import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        w,h,n = list(map(int,input().split()))

        ini = 1
        while w%2==0:
            w//=2
            ini*=2
        while h%2==0:
            h//=2
            ini*=2
        if ini>=n:
            yield 'YES'
        else:
            yield 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
