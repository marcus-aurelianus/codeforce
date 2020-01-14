lst= [2,10,12,600,1000]
maxr=[]
minr= float('Inf')
res=[]
for kap in range(1,1000):

    temp=0
    for ele in lst:
        
        temp=max(temp,kap^ele)

        #print(kap,ele,kap^ele)

    if temp<minr:
        res=kap
    minr=min(minr,temp)

print(minr,res) 
