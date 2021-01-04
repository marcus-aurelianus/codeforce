import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from bisect import bisect_left
def gift():
    for _ in range(t):
        n = int(input())
        maxs = []
        mins = []
        nums = []
        for i in range(n):
            ele = list(map(int,input().split()))
            ele.sort()
            nums.append(ele)
            maxs.append([ele[1],i])
            mins.append([ele[0],i])

        maxs.sort()
        mins.sort()


        ansRaw = {}
        for num in mins:
            if maxs[0][0]<nums[num[1]][1] and nums[maxs[0][1]][0]<num[0]:
                ansRaw[num[1]]=maxs[0][1]+1
            else:
                ansRaw[num[1]]=-1
        ans = []

        for i in range(n):
            ans.append(ansRaw[i])
        yield " ".join([str(x) for x in ans])
            

                
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
