import random
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))
for i in range(1000):
    for j in range(2,50):
        arry = []
        n=j
        for k in range(n):
            arry.append(random.randint(1,10**9))

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
                        if (factor-curr)<minDiff:
                            minDiff=factor-curr
                            toappend=curr
                else:
                    diffF = curr//last

                    diff1 = curr%last
                    diff2 = (diffF+1)*last-curr
                    if diff1>diff2:
                        toappend = (diffF+1)*last
                    else:
                        toappend = diffF*last
                ans.append(toappend)
        
        diff = 0
        
        for i in range(n):
            diff += abs(arry[i]-ans[i])
        
        if (sum(arry)<2*diff):
            print(arry)
            print(sum(arry))
            print(ans)
            print(diff)
