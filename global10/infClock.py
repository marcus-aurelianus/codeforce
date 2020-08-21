import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        arry = list(map(int,input().split()))

        

        if k%2:
            maxn=max(arry)
            yield " ".join(str(x) for x in map(lambda x:maxn-x,arry))
        else:
            minn=min(arry)
            yield " ".join(str(x) for x in map(lambda x:x-minn,arry))
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 1 2 3 4





# 0 6 1 3 5
# 6 0 5 3 1


# 5 -1 4 2 0
# 0 6 1 3 5


# 5 1 4 2 1
# 0 4 1 3 4
# 4 0 3 1 0
