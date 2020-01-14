for a in range(1,1001):
    for b in range(1,1001):
        res=0
        for i in range(1,a+1):
            for j in range(1,b+1):
                if i*j+i+j==int(str(i)+str(j)):
                    res+=1
        if (a*(len(str(b))-1))!=res:
            print(a,b,res,a*(len(str(b))-1))
