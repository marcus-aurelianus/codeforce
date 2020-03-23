for i in range(1,100000):
    num=int((i-2)*'9'+'23')
    if num%9==0 or num%2==0 or num%3==0:
        print(num)
    
