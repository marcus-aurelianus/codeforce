a = int(input())
 
AS = format(a,'b').zfill(6)
#print (AS)
 
ans = [0,0,0,0,0,0]
 
ans[0] = AS[0]
ans[1] = AS[5]
ans[2] = AS[3]
ans[3] = AS[2]
ans[4] = AS[4]
ans[5] = AS[1]
 
#print (ans)
 
n = 0
for i in range(6):
    n *= 2
    n += int(ans[i])
print (n)
