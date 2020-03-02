for n in range(1,9):
    for i in range(1,n+1):
        for j in range(1,n+1):
            r1,r2 = i,j
            sum1=r1+r2
            print(n,i,j)
            if sum1<n:
                maxres=1
                minres=sum1-1
            elif sum1==n:
                maxres=1
                minres=n-1
            else:
                maxres=min(sum1-n+1,n)
                minres=n
            if sum1==3:
                print( "2 2")  
            elif sum1==2:
                print( "1 1")  
            else:
                print( str(maxres)+" "+str(minres))
        
      
