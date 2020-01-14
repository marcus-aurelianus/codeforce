def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

n = int(input())
nums = [int(ele) for ele in input().split()]

res=0
for i in range(n-1):
    for j in range(i,n):
        res=max(res,compute_lcm(nums[i],nums[j]))
print(res)
        
