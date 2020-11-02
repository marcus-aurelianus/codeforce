import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        an = list(map(int,input().split()))
        bn = list(map(int,input().split()))

        left = []
        maxTime = 0
        timeSpend = 0
        for i in range(n):
            if an[i]<=bn[i]:
                maxTime = max(an[i],maxTime)
            else:
                left.append([an[i],bn[i]])
        fleft = []
        for ele in left:
            if ele[0]>maxTime:
                fleft.append(ele)
        fleft.sort(key=lambda x:(-x[0],-x[1]))
        #print(fleft)
        for ele in fleft:
            ani,bni = ele
            #print(ani,bni,timeSpend)
            if bni+timeSpend<ani:
                timeSpend+=bni
                maxTime=max(maxTime,timeSpend)
            else:
                maxTime=max(ani,maxTime)
            #print(maxTime)
        yield maxTime
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 5
# 18 14 12 10 8
