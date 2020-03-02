import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n=int(input())
skyies = [int(x) for x in input().split()]
res=[]
if n<=2:
    res=skyies
    print(" ".join(str(x) for x in res))
else:
    res.append(skyies[0])
    for i in range(n-2):
        kappa=res[-1]
        if skyies[i+2]>skyies[i+1] and kappa>skyies[i+1]:
            if skyies[i+2]>kappa:
                res.pop()
                res.append()

        


##1 4 
##2 5 
##5 1
##4 3
##3 1
##4 6
##3 7
##1 1
            
