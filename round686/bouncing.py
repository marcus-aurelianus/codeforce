import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        
        n,p,k = list(map(int,input().split()))
        array = input()
        x,y = list(map(int,input().split()))
        f = [0] * n
        for i in range(n-1,-1,-1):
            if array[i]=='0':
                f[i]+=1
            if i+k<n:
                f[i]+=f[i+k]
        ans = float("inf")
        for i in range(n-p+1):
            w = y*i + x*f[i+p-1]
            if ans>w:
                ans = w
        yield ans
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#####
###x#
#####111111010 9 9 7 22 1 0 22
