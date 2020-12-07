import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))

        got1 = False
        dic = defaultdict(lambda:0)
        diu = {}
        curr = 0
        maxNum = 0
        for i in range(n):
            dic[array[i]]+=1
            maxNum = max(maxNum,dic[array[i]])
            if i>0:
                if array[i]<array[i-1]:
                    curr+=1
              
                else:
                    if curr>0:
                        diu[curr]=True
                    curr=0
        print(curr)
        ans = [1]*n
        for i in range(maxNum-1):
            ans[i]=0
        for ele in diu:
            ans[ele]=0
        yield ans,diu
            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

# 1 3 4 5 2
# 
#"{} {} {}".format(maxele,minele,minele)
