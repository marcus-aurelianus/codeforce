import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        dic = {}
        for i in range(k):
            posx,posy = list(map(int,input().split()))
            if posx!=posy:
                dic[posx]=posy
        gone = {}
        ans = 0
        #print(dic)
        for ele in dic:
            if not gone.get(ele,False):
                fromPos = ele
                while True:
                    gone[fromPos] = True
                    #print(dic,fromPos)
                    toPos = dic.get(fromPos,False)
                    if not toPos:
                        break
                    else:
                        ans+=1
                    fromPos = toPos
                    #print(fromPos,ele)
                    
                        
                    if fromPos == ele:
                        ans+=1
                        break
                    else:
                        if gone.get(fromPos,False):
                            break
        yield ans
                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
