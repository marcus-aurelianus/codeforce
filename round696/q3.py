import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import Counter

def gift():
    for _ in range(t):
        N = int(input())
        A = list(map(int,input().split()))
        A.sort()

        C= Counter(A)
        am = max(A)

        for i in range(2*N-1):
            Ad = A[:-1]
            Ad.remove(A[i])
            res = [(A[i], am)]
            pp = A[i] + am
            C = Counter(Ad)

            x = am

            for _ in range(N-1):
                while Ad and C[Ad[-1]]==0:
                    Ad.pop()
                d = Ad.pop()
                C[d] -= 1
                if C[x-d]==0:
                    break
                C[x-d] -= 1
                res.append((d,x-d))
                x = max(d,x-d)
            else:
                yield 'YES'
                yield str(pp)
                for a  in res:
                    yield ' '.join([str(x) for x in a])
                break
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
