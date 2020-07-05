from itertools import chain, combinations
import math
print(math.log(16,2))
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))

for i in range(100):
    kap=list(range(1,i+2))
    ans=0
    subset=powerset(kap)
    for sub in subset:
        n=len(sub)
        if n==1:
            ans+=1
        else:
            temp=sub[0]
            correct=True
            for j in range(1,n):
                next1=temp^sub[j]
                #print(sub,temp,next1)
                if next1>temp:
                    temp=next1
                else:
                    correct=False
                    break
            if correct:
                ans+=1
    print(i+1,ans)
