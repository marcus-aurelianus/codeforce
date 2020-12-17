import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        ans = [arry[0]]

        for i in range(1,n):
            last = ans[-1]
            curr = arry[i]
            if last%curr ==0 or curr%last==0:
                ans.append(curr)
            else:
                toappend = None
                minDiff = float("inf")
                if last>curr:
                    Lfactors = sorted(list(factors(last)))
                    for factor in Lfactors:
                        if (abs(factor-curr))<minDiff:
                            minDiff=abs(factor-curr)
                            toappend=factor
                else:
                    diffF = curr//last

                    diff1 = curr%last
                    diff2 = (diffF+1)*last-curr
                    if (diffF+1)*last>10**9:
                        toappend = diffF*last
                    else:
                        if diff1>diff2:
                            toappend = (diffF+1)*last
                        else:
                            toappend = diffF*last
                ans.append(toappend)
        yield " ".join([str(x) for x in ans])
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
