n=int(input())
nums=[int(ele) for ele in input().split()]

maxn=max(nums)
if maxn==0:
    print(0)
else:
    print(2**(len(bin(maxn)[2:])-1))
