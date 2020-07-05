import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n=int(input())
a = list(map(int,input().split()))
dic = {}
dic[0] = -1
nsum = 0
ans = 0
ll = -2
 
for i in range(n):
 
    nsum += a[i]
 
    if nsum  in dic:
        ll = max(dic[nsum] , ll)
    ans += i-ll-1
    dic[nsum] = i

 
    #print (ll,ans)
 
print (ans)


            

