import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        A = [int(a) - 1 for a in input().split()]
        C = [0] * n
        for a in A:
            C[a] += 1
        l, r = 0, n - 1
        for i in range(n):
            if C[i] != 1:
                break
            if A[l] == i:
                l += 1
            elif A[r] == i:
                r -= 1
            else:
                break

        a0 = min(C)
        k = min(i + 1, n - 1) if C[i] else i
        ans = str(a0) + "0" * (n - k - 1) + "1" * (k)
        yield ans

            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

# 1 2 3 3 3
# 0 0 0 1
#"{} {} {}".format(maxele,minele,minele)
