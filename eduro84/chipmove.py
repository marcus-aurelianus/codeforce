import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



if __name__ == '__main__':
    n,m,k= list(map(int,input().split()))

    for i in range(k):
        pos1=list(map(int,input().split()))

    for i in range(k):
        pos2=list(map(int,input().split()))
    ans = ["L"] * (m-1) + ["U"] * (n-1)
     
    for i in range(m):
     
        if i % 2 == 0:
            ans += ["D"] * (n-1)
        else:
            ans += ["U"] * (n-1)
     
        if i != m-1:
            ans += ["R"]
     
    print (len(ans))
    print ("".join(ans))

