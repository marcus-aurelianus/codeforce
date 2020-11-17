import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        array = list(map(int,input().split()))

        array.sort()
        diff = n-math.ceil(n/2)
        ans = 0
        for i in range(k):
            
            ans += array[n*k-1-((diff+1)*i+diff)]
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
