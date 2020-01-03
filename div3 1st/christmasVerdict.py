from copy import deepcopy
import time
if __name__ == '__main__':
    start=time.time()
    n, m = map(int,input().split())
    trees=[int(x) for x in input().split()]
    peopleNtree={int(x):True for x in trees}
    people=[]
    #check max fill between max and min ele
    minTree=min(trees)
    maxTree=max(trees)
    maxDis=maxTree-minTree

    maxFill=maxDis//2*4-1+maxDis%2-(len(trees)-2)
    #preVal
    distance=-1
    pos=0
    totalDistance=0

    while m>0:

        treeVacancy=trees[pos]+distance
        exist=peopleNtree.get(treeVacancy,False)
        if not exist:
            peopleNtree[treeVacancy]=True
            people.append(treeVacancy)
            totalDistance+=abs(distance)
            m-=1
        if distance>0:
            pos+=1
        distance*=-1
        if pos==n:
            pos=0
            distance=distance-1

    print(totalDistance)
    print(" ".join(map(str,people)))
    end=time.time()
    print(end-start)
