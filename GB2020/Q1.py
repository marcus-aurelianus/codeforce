import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))

        dic={}
        for i in range(n):
            for j in range(i+1,n):
                dic[A[j]-A[i]]=True
        yield len(dic)


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
