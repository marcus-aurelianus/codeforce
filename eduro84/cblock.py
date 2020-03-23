import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
n=5
counter={}
for i in range(n):
    counter[i+1]=0
for i in range(10**n):
    
    
    if i !=0:
            
        strnum=str(i)
        strfull='0'*(n-len(strnum))+strnum
        currlen=1
        for j in range(n-1):
            #print(i,counter)
            if strfull[j]!=strfull[j+1]:
                if j==n-2:
                    freq2=counter[1]
                    counter[1]=freq2+1
                freq1=counter[currlen]
                counter[currlen]=freq1+1
                currlen=1
            elif j==n-2:
                currlen+=1
                freq1=counter[currlen]
                counter[currlen]=freq1+1
            else:
                currlen+=1
    else:
        counter[n]+=1
print(counter)

