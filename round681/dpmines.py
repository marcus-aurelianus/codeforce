import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        mines = input()
        currCost = 0
        currZero = 0
        for mine in mines:
            if mine=='1':
                if currZero==0:
                    if currCost==0:
                        currCost+=a
                else:
                    if a>=b*(currZero):
                        currCost+=b*(currZero)
                    else:
                        currCost+=a
                currZero=0
            else:
                if currCost!=0:
                    currZero+=1
        yield currCost
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 5
# 18 14 12 10 8
