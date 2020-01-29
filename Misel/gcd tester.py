import math
m,n=20,0
    
for i in range(1,m):
    for j in range(i,m):
        temp=math.gcd(i,j)
        res=0
        tes=[]
        for x in range(j):
            temp1=math.gcd(i+x,j)
            if temp1==temp:
                res+=1
                tes+=[i+x]
        print(i,j,res," ",temp,tes)
                
            

    
    
