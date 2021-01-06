import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n,x = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        dude = []
        for ele in arry:
            cout = 0
            while True:
                if ele%x==0:
                    cout+=1
                    ele//=x
                else:
                    break
            dude.append(cout)
            
        minD = min(dude)
        tillMind = False
        ans=0
        for i in range(n):
            ele = dude[i]
            if ele>minD:
                if tillMind:
                    ans+=(minD+1)*(arry[i])
                else:
                    ans+=(minD+2)*(arry[i])
            else:
                tillMind = True
                ans+=(minD+1)*(arry[i])
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
