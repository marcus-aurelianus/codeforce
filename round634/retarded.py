import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
    
        
#print(len(inamo))
def gift():
    for _ in range(t):
        dog=[]
        for i in range(9):
            kap=list(input())
            dog.append(kap)
        dog[0][0]=dog[0][1]
        dog[1][3]=dog[1][4]
        dog[2][6]=dog[2][7]
        dog[3][1]=dog[3][2]
        dog[4][4]=dog[4][5]
        dog[5][7]=dog[5][8]
        dog[6][2]=dog[6][3]
        dog[7][5]=dog[7][6]
        dog[8][8]=dog[8][0]
        for i in range(9):
            yield "".join(str(x) for x in dog[i])
 
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
    

