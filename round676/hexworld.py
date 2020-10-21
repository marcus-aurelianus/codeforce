import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        tx,ty = list(map(int,input().split()))
        c1,c2,c3,c4,c5,c6 = list(map(int,input().split()))
        dic = [[1,1],[0,1],[-1,0],[-1,-1],[0,-1],[1,0]]

        if tx>0:
            if ty>0:
                if tx>ty:
                    cost1 = c2*ty + c6*tx
                    cost2 = (tx-ty)*c5 + c1*tx
                    cost3 = ty*c1 + (tx-ty)*c6 
                elif tx<ty:
                    cost1 = (ty-tx)*c2+tx*c1
                    cost2 = ty * c2 + tx *c6
                    cost3 = ty * c1 + (ty-tx) * c3
                else:
                    cost1 = tx * c1
                    cost2 = tx * c2 + tx * c6
                    cost3 = tx * c2 + tx * c6               
            elif ty==0:
                cost1 = tx * c6
                cost2 = tx * c1 + tx * c5
                cost3 = tx * c1 + tx * c5 
            else:
                cost1 = abs(ty)*c5+tx*c6
                cost2 = c5*(tx-ty)+c1*(tx)
                cost3 = c6*(tx-ty)+c4*(abs(ty))

        elif tx<0:
            if ty>0:
                cost1 = c2 * ty + abs(tx)*c3
                cost2 = (ty-tx) * c2 + abs(tx) * c4
                cost3 = c1 * ty + (ty-tx)*c3
            elif ty==0:
                cost1 = abs(tx) * c3
                cost2 = abs(tx) * (c2 + c4)
                cost3 = abs(tx) * (c2 + c4)
            else:
                if tx>ty:
                    cost1 = c6 * (tx-ty) + (-ty) * c4
                    cost2 = (tx-ty)*c5 + (-tx)*c4
                    cost3 = (-ty) * c5 + c3 *(-tx)
                elif tx<ty:
                    cost1 = (ty-tx)*c3 + (-ty)*c4
                    cost2 = (-tx)*c3 + (-ty)*c5
                    cost3 = (-tx)*c4 + (ty-tx)*c2
                else:
                    cost1 = (-tx)*c4
                    cost2 = (-tx)*(c3+c5)
                    cost3 = (-tx)*(c3+c5)
        else:
            if ty>0:
                cost1 = c2*ty
                cost2 = (c1+c3)*ty
                cost3 = (c1+c3)*ty
            elif ty==0:
                cost1 = 0
                cost2 = 0
                cost3 = 0
            else:
                cost1 = c5*(-ty)
                cost2 = (c4+c6)*(-ty)
                cost3 = (c4+c6)*(-ty)
        yield min(cost1,cost2,cost3)

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
