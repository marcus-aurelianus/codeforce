import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,y,k = list(map(int,input().split()))
        requirex = k*(y+1)-1
        ans=requirex//(x-1)+k

        if requirex%(x-1):
            ans+=1
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
