def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


fib1=[1,1]

for i in range(80):
    if i>=2:
        temp=fib1[-1]+fib1[-2]
        fib1.append(temp)

print(fib1[-1])
