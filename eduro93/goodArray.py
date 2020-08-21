import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        string = input()
        ans=[0]*(n+1)
        res=0
        
        dic=defaultdict(lambda:0)
        dic[0]=1
        
        for i in range(n):
            ans[i+1]=ans[i]+int(string[i])
            dic[ans[i+1]-(i+1)]+=1
        print(dic)
        for i in dic:
            #print(dic[i],dic,i)
            res += dic[i] * (dic[i]-1) // 2
        yield res
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 0 1 2 3
