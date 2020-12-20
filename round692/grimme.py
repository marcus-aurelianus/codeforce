import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

string = input()
x,y = list(map(int,input().split()))

n = len(string)

curr = [[0,0,0]]*n
for i in range(n):
    if i==0:
        if string[n-1-i]=='0':
            curr[n-1-i][0]=1
        elif string[n-1-i]=='1':
            curr[n-1-i][1]=1
        else:
            curr[n-1-i][2]=1
    else:
        z,o,q=curr[n-i]
        if string[n-1-i]=='0':
            curr[n-1-i]=[z+1,o,q]
        elif string[n-1-i]=='1':
            curr[n-1-i]=[z,o+1,q]
        else:
            curr[n-1-i]=[z,o,q+1]

px = 0
py = 0
ans = 0
for i in range(n-1):
    n0,n1,np = curr[i+1]
    if string[i]=='1':
        if n0!=0:
            ans += (n0+np)*y
    elif string[i]=='0':
        if n1!=0:
            ans += (n1+np)*x
    else:
        if n0==0 or n1==0:
            ans+=0
        else:
            ans+=min((n1+np)*y,(n0+np)*x)



print(ans)


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
# 111???000???111
