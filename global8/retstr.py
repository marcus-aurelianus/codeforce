import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

K = int(input())


S = 'codeforces'
 
arr = [1]*10
 
for _ in range(1000):
    res = 1
    for a in arr:
        res *= a
    if res >= K:
        break
    arr[arr.index(min(arr))] += 1
    
    
 
ans = ''
for i in range(10):
    ans = ans + S[i]*arr[i]
print(ans)
            
# a b
# a a+b
# 2a+b a+b
# 2a+b 3a+2b
# 5a+3b 3a+2b
# 5a+3b 8a+5b
# 13a+8b 7a+5b
# 11a+8b 18a+13b
            

#codeforcessss

#codefroceess




#codeforces

