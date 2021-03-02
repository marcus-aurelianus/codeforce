import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))

        arr.sort()
        dic = defaultdict(lambda:0)

        for ele in arr:
            dic[ele]+=1
            
        curr = arr[-1]
        dic[curr]-=1

        start = n-1
        steps = []
        while (steps<n-1):
           if arr[start] 
        yield dic
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])

