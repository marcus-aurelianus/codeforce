import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        p,a,b,c = list(map(int,input().split()))
        if p%a==0 or p%b==0 or p%c==0:
            yield 0
        else:
            yield min((a-(p % a)),(b-(p % b)),(c-(p % c)))
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
