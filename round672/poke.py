import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n, q = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        ops = []
        for i in range(q):
            op = list(map(int,input().split()))
            ops.append(op)
        station = [0] * n
        station[-1]=arry[n-1]
        ans = arry[n-1]
        for i in range(n-1):
            if arry[n-1-i]<arry[n-2-i]:
                tem = arry[n-2-i]-arry[n-1-i]
                station[n-2-i]= tem
                ans += tem
        yield ans

        for i in range(q):
            s, e = ops[i]
            sNum, eNum = arry[s-1],arry[e-1]
            arry[s-1],arry[e-1] = arry[e-1],arry[s-1]
            if s>1:
                ans-=station[s-2]
                station[s-2]=0
                if arry[s-1]<arry[s-2]:
                    tem = arry[s-2]-arry[s-1]
                    station[s-2]= tem
                    ans += tem
  
            ans-=station[s-1]
            station[s-1]=0
            if arry[s]<arry[s-1]:
                tem = arry[s-1]-arry[s]
                station[s-1]= tem
                ans += tem

            if e==n:
                ans-=station[n-1]
                station[n-1]=sNum
                ans+=sNum
            elif e-s>1:
                ans-=station[e-2]
                station[e-2]=0
                if arry[e-1]<arry[e-2]:
                    tem = arry[e-2]-arry[e-1]
                    station[e-2] = tem
                    ans += tem
      

            if e<n:
                ans-=station[e-1]
                station[e-1]=0
                if arry[e]<arry[e-1]:
                    tem = arry[e-1]-arry[e]
                    station[e-1] = tem
                    ans += tem
        
            
            yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)




# 0 0 0 1 1 1 7


# 9 8 1 7 2 

# 1 3 3
# 1 3 2

# 1 2 3
# 1 2 3

# 2 2 3
# 2 1 3
