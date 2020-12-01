import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        curr=0
        i=0
        while True:
            if curr>=n:
                break
            else:
                i+=1
                curr+=i

        for ai in range(i,0,-1):
            if (curr-(ai+1))>=n:
                curr-=(ai+1)

        yield i+(curr-n)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
