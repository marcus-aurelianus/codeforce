import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input()) 

        nums = list(map(int,input().split()))

        dic = {}
        for ele in nums:
            dic[ele]=True
        ans = 0
        for i in range(n,n*2):
            if not dic.get(i,False):
                ans+=1
        yield max(ans,1)
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
