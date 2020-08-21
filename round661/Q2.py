import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry1 = list(map(int,input().split()))
        arry2 = list(map(int,input().split()))
        a=min(arry1)
        b=min(arry2)
        ans=0
        for i in range(n):
            ans+=(max(arry1[i]-a,arry2[i]-b))
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 5 4 2 3
