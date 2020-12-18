import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        b = []
        for i in range(n):
     
            d = a[i].bit_length()
     
            M = 2**d
            m = 2**(d-1)
     
            if abs(M-a[i]) <= abs(m-a[i]) and M <= 10**9:
                b.append(M)
            else:
                b.append(m)


        yield " ".join([str(x) for x in b])


                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
