import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import copy

def gift():
    for _ in range(t):

        n, k , l=list(map(int,input().split()))
        arry = list(map(int,input().split()))

        
        prevdis=float("inf")
        increase=False
        for val in arry:
            if val>l:
                break
            dis=l-val

            if dis>=k:
                prevdis=dis
                increase=False
                continue
            if increase:
                if dis>=prevdis+1:
                    prevdis+=1
                else:
                    break
            else:
                prevdis=min(prevdis-1,dis)
                if prevdis==0:
                    increase=True
        else:
            yield 'Yes'
            continue
        yield 'No'
                    
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
