if __name__ == '__main__':
    n= int(input())
    lst1=[]
    lst2=[]
    lst3=[]
    for i in range(n):
        lst1.append([int(x) for x in input().split(" ")])
        lst2.append([int(x) for x in input().split(" ")])
        lst3.append([int(x) for x in input().split(" ")])
    for i in range(n):
        stackLoc={}
        for j in range(len(lst2[i])):
            stackLoc[lst2[i][j]] = j+1
        sec=0
        counter=0
        checked=1
        #print(stackLoc)
        for ele in lst3[i]:
            loc=stackLoc[ele]
            if loc<checked:
                sec+=1
            else:
                sec+=((loc-counter-1)*2+1)
            checked=max(checked,loc)
            counter+=1
        print(sec)
            
