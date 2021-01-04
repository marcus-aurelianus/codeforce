import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from bisect import bisect_left
def gift():
    for _ in range(t):
        n = int(input())

        nums = []
        for i in range(n):
            ele = list(map(int,input().split()))
            ele.sort()
            ele.append(i)
            nums.append(ele)
        nums.sort(key = lambda x: (x[0], x[1]))

        currMinMax = float("inf")

        level = nums[0][0]
        temMin = float("inf")
        ansMap={}
        prevLoc = None
        temPrevLoc = None
        for ele in nums:
            mine,maxe,index = ele
            if mine != level:
                level = mine
                if temMin<currMinMax:
                    currMinMax = temMin
                    prevLoc = temPrevLoc
                
            if maxe>currMinMax:
                ansMap[index]=prevLoc+1
            else:
                ansMap[index]=-1
                
            if maxe<temMin:
                temMin=maxe
                temPrevLoc=index

        ans = []
        for i in range(n):
            ans.append(ansMap[i])
        yield " ".join([str(x) for x in ans])

                
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
