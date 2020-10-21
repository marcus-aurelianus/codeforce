import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split())) 
        array = input() 
        dic = defaultdict(lambda:0)
        dicLis = []
        curr = 0
        win = 0
        score = 0
        for i in range(n):
            if array[i]=="W":
                if win>0:
                    score+=2
                else:
                    score+=1
                win += 1
                dicLis.append(curr)
                curr=0
            else:
                win = 0
                curr+=1
        dicLis.append(curr)

        for i in range(1,len(dicLis)-1):
            if dicLis[i]:
                dic[dicLis[i]]+=1
        itemRino = sorted(list(dic.items()))

        for ele in itemRino:
            gap, count = ele
            while count:
                
                if k>=gap:
                    score += gap*2+1
                else:
                    score += k*2
                count-=1
                k -= gap
                #print(gap,k,score)
                if  k<=0:
                    break
            if k<=0:
                break
        if k>0:
            if len(dicLis)>1 and dicLis[-1]>0:
                score += 2*(min(k,dicLis[-1]))
                k-=dicLis[-1]
        if k>0:
            if len(dicLis)>1:
                score += 2*(min(k,dicLis[0]))
                k-=dicLis[0]
            else:
                score += 2*(min(k,dicLis[0]))-1
        yield score

            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
