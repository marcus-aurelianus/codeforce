#C(M,N-1)==(math.factorial(M)//(math.factorial(N-1))//math.factorial(M-N+1))

for i in range(1,n):
    ans=ans*(m-i+1)%mod*power(i,mod-2)%mod
