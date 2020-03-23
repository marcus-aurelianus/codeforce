import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
sum1=10
currnum=0
ans=[10]
mod=998244353
n=int(input())
for i in range(1,n):
    #print(sum1,10**(i+1)*(i+1))
    currnum=(9*i+10)*pow(10,i,mod)-sum1
    sum1+=currnum
    ans.append(currnum%mod)
print(" ".join(str(x) for x in ans[::-1]))
