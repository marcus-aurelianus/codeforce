import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
 
n, m = list(map(int,input().split()))
s = input()
t = input()
if n==m or m==1:
    print(1)
else:
    indexes = [0]*m
    revIndexes = [0]*m
    front,back = 0,n-1
    for i in range(m):
        while s[front]!=t[i]:
            front += 1
        indexes[i] = front
        front += 1
        while s[back]!=t[m-1-i]:
            back -= 1
        revIndexes[m-1-i] = back
        back -= 1
    ans = 1
    #print(indexes,revIndexes)
    for i in range(m-1):
        ans = max(ans,revIndexes[i+1]-indexes[i])
    print(ans)
