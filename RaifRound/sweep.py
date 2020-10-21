

n = int(input())
s = input()

tot=0
cur=0

hist=[0]*(n)

i=0

while (i<n):
    if (s[i]=='0'):
        tot+=cur
    else:
        l=i
        r=i
        while (r+1<n and s[r+1]=='1'): r+=1
        
        for x in range(r-l+1):
            cur+=(l+x+1)-hist[x]
            #print(x,l+x,cur)
            tot+=cur
            hist[x]=r-x+1
            #print(hist,r)
        i=r
    i+=1


print(tot)
