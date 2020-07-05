n=100
ans=[]
for i in range(1,n+1):
    counter=0
    for j in range(1,i+1):
        lenn=len(bin(i)[2:])
        curr=bin(j)[2:]
        prev=bin(j-1)[2:]
        lencur=len(curr)
        lenprev=len(prev)
        curr=(lenn-lencur)*'0'+curr
        prev=(lenn-lenprev)*'0'+prev


        for m in range(lenn):
            if curr[m]!=prev[m]:
                counter+=1
    ans.append(counter)
    print(i,counter)

##for i in range(1,n):
##    print(ans[i]-ans[i-1])
        
