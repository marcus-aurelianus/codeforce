import bisect

def ascent(list1,len1):
    if len1==1:
        return False
    for i in range(len1-1):
        if list1[i+1]>list1[i]:
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    kappa=0
    nmsl=[]
    minList=[]
    maxList=[]
    for i in range (n):
        fulllist=[int(ele) for ele in input().split()]
        lenl=fulllist[0]
        lst=fulllist[1:]
        minL = min(lst)
        maxL = max(lst)
        
        ascentYN = ascent(lst,lenl)
        if ascentYN:
            kappa+=1
        else:
            nmsl.append([minL,maxL])
            minList.append(minL)
            maxList.append(maxL)
    res=kappa*(2*n-kappa)
    
    count1=0
    minList.sort()
    maxList.sort()
    #sortedMinL=qsort(minList)
    #sortedMaxL=qsort(maxList)
    minList.reverse()
    maxList.reverse()
    maxList.append(float("-inf"))
    print(minList,maxList)
    maxind=0
    for ele in minList:
        while ele <maxList[maxind]:
            maxind+=1
        res+=maxind

    print(res)
        
