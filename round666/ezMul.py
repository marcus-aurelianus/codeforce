import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

            
n = int(input())

arry = list(map(int,input().split()))

if n==1:
    print("1 1")
    print(1)
    print("1 1")
    print(1)
    print("1 1")
    print(-arry[0]-2)
else:
    print("1 {}".format(n-1))
    tem = []
    for i in range(n-1):
        tem.append(arry[i]*(n-1))

    print(" ".join(str(x) for x in tem))

    print("{} {}".format(n,n))
    print(arry[n-1]*(n-1))


    print("1 {}".format(n))
    temRes = []
    for i in range(n):
        temRes.append(-arry[i]*(n))
    print(" ".join(str(x) for x in temRes))


#1 3 2 4
#1 12 8 12
#4 
