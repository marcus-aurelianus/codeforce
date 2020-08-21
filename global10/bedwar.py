import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n = int(input())
        lst = list(input())
        ans=0

        leftP=[]
        rightP=[]
        for i in range(n):
            
            if i==0:
                left=lst[-1]
            else:
                left=lst[i-1]
            if i==n-1:
                right=lst[0]
            else:
                right=lst[i+1]
            if left=="L":
                if right=="L":
                    if lst[i]!="R":
                        ans+=1
                        leftP.append(i)

            else:
                if right=="R":
                    if lst[i]!="L":
                        ans+=1
                        rightP.append(i)
            
            def checkPart(param,n):
                if not param:
                    return 0
                res=0
                consectlen=1
                s,e=0,len(param)-1
                if e==s:
                    return 1
                tempe=e
                checked=False
                while s<e and s<tempe :
                    
                    if param[s]==0 and param[e]==n-1 and not checked:
                        
                        if param[tempe]-1==param[tempe-1]:
                            tempe-=1
                            consectlen+=1
                        else:
                            tempe-=1
                            e=tempe
                            consectlen+=1
                            checked=True
                    else:
                        #print(s,e)
                        if param[s]+1==param[s+1]:
                            s+=1
                            consectlen+=1
                        else:

                            res+=math.ceil(consectlen/3)
                            s+=1
                            consectlen=1
                #print(consectlen,s,e)
                res+=math.ceil(consectlen/3)
                return res
        #print(leftP,rightP)     
        yield checkPart(leftP,n)+checkPart(rightP,n)
                
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 1 2 3 4





# 0 6 1 3 5
# 6 0 5 3 1


# 5 -1 4 2 0
# 0 6 1 3 5


# 5 1 4 2 1
# 0 4 1 3 4
# 4 0 3 1 0




# 1 4 5 3 2 1

# 
