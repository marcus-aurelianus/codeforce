import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        leftRight = []
        topBottom = []

        for i in range(n):
            temArray = list(map(int,input().split()))
            leftRight.append(temArray)

        for i in range(m):
            temArray = list(map(int,input().split()))
            topBottom.append(temArray)            
        ansIndex = []
        ans = []
        firstLineDic = {}
        for i in range(n):
            firstLineDic[leftRight[i][0]] = i
        
        for i in range(m):
            #print(firstLineDic.get(topBottom[i][0],'tt'))
            if firstLineDic.get(topBottom[i][0],'tt')!='tt':
                #print(i)
                for ele in topBottom[i]:
                    yield " ".join([str(x) for x in leftRight[firstLineDic[ele]]])
                break

   

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
