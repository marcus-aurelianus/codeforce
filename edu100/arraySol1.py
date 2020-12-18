import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))

        B = []
        C = []
        for i in range(n):
            if i%2==0:
                B.append(1)
                C.append(A[i])
            else:
                B.append(A[i])
                C.append(1)
        X = 0

        for i in range(n):
            X+=2*abs(B[i]-A[i])

        if X<=sum(A):
            yield " ".join([str(x) for x in B])
        else:
            yield " ".join([str(x) for x in C])


                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
