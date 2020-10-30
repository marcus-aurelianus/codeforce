import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        array = sorted(list(map(int,input().split())))
        dic = defaultdict(lambda:0)
        for ele in array:
            dic[ele] += 1

        reOrderItems = list(dic.items())
        newOrder = []
        for ele in reOrderItems:
            newOrder.append([ele[0]-ele[1]//2,ele[0],ele[1]])
        newOrder.sort(key=lambda x:x[0])
        ans=0
        curr=0
        #print(newOrder)
        dic = {}
        for item in newOrder:

            if curr < item[1]-item[2]//2:
                for i in range(item[1]-item[2]//2,item[1] + (item[2]-1)//2 + 1):
                    ans += abs(i-item[1])
                    dic[i] = True
                curr = item[1] + (item[2]-1)//2
            else:
                index = 0
                counter = 0
                while (counter<item[2]):
                    currI = curr+1+index

                    
                    revcurrI = item[1]- abs(currI-item[1])
                    breaker = False
                    for dis in range(item[1]-revcurrI+1):
                        weareAt = item[1]-dis
                        if (weareAt>=1 and not dic.get(weareAt,False)):
                            ans += abs(weareAt-item[1])
                            counter+=1
                            dic[weareAt]=True
                        if counter == item[2]:
                            breaker = True
                            break
                    if breaker:
                        break
                    if (not dic.get(currI,False)):
                        dic[currI] = True
                        ans += abs(currI-item[1])
                        counter+=1
                    index += 1
                    
                curr = curr+item[2]
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
