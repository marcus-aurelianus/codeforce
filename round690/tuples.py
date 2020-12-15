import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        dic = defaultdict(lambda:0)
        for ele in array:
            dic[ele]+=1
        ans = 0
        for i in range(1,n+1):
            for j in range(i,i+3):
                for k in range(j,i+3):
                    if i==j and j==k:
                        if dic[i]>=3: 
                            ans+=(dic[i]*(dic[i]-1)*(dic[i]-2))//6
                    elif i==j and j!=k:
                        if dic[i]>=2 and dic[k]>0:
                            ans+=(dic[i]*(dic[i]-1))//2*(dic[k])
                    elif j==k:
                        if dic[j]>=2 and dic[i]>0:
                            ans+=(dic[j]*(dic[j]-1))//2*(dic[i])
                    else:
                        if dic[i]>0 and dic[j]>0 and dic[k]>0:
                            ans+=dic[i]*dic[j]*dic[k]
                            
                        
        yield ans
                            
                        


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
    
# 5 1 2 4 5 1 6 4 2
