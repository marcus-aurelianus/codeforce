import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        if n==1:
            yield 'YES'
        else:
            ans=True
            arry.sort()
            for i in range(n-1):
                if arry[i+1]-arry[i]>1:
                    ans=False
                    break
            yield 'YES' if ans else 'NO'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 5 4 2 3
