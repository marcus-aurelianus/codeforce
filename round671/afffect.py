import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n ,x = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        rem = []
        for i in range(n):
            if arry[i] != x:
                rem.append(arry[i])
        if len(rem)==0:
            yield 0
        elif abs(sum(arry)/n-x)<0.1**10 or len(rem)!=n:
            yield 1
        else:
            yield 2
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
