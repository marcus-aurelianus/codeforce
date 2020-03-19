import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
 
if __name__ == '__main__':
    n,mod = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    ans=1
    if n > mod:
        print (0)
    else:
        for i in range(n):
                for j in range(i):
                    ans*=abs(nums[i]-nums[j])
                    ans%=mod
        print(ans)
