import math
a,b=[int(ele) for ele in input().split()]
inamo=10**9+7
res=(int(math.factorial(a+b*2-1)//math.factorial(a-1)//math.factorial(b*2)))%inamo
print(res)
