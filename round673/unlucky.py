import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        array = list(map(int,input().split()))
        dic1 = defaultdict(lambda:[])
        ans = [0] * n
        first = True
        for i in range(n):
            if array[i]==k/2:
                if first:
                    ans[i] = 1
                    first = False
                else:
                    first = True
            elif len(dic1[k-array[i]])==0:
                dic1[array[i]].append(i)
                ans[i] = 1
                

       
        yield " ".join([str(x) for x in ans])
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
