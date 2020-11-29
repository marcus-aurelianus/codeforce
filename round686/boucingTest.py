import random
def bounceAlgro(n,p,k,array,x,y):
    minCost = float("inf")
    f = [0] * n
    for i in range(n-1,-1,-1):
        if array[i]=='0':
            f[i]+=1
        if i+k<n:
            f[i]+=f[i+k]
    ans = float("inf")
    for i in range(n-p+1):
        w = y*i + x*f[i+p-1]
        if ans>w:
            ans = w
    return ans
def naiveAlgro(n,p,k,array,x,y):
    minCost = float("inf")
    for i in range(n-p+1):
        currCost = i*y
        j = p+i-1
        while j<n:
            if array[j]=='0':
                currCost += x
            j+=k
        minCost = min(currCost, minCost)
    return minCost
for n in range(1,10):
    for p in range(1,n+1):
        for k in range(1,n+1):
            array = ""
            for i in range(n):
                array += str(random.randint(0, 1))
            x = random.randint(1, 100)
            y = random.randint(1, 100)
            ans = bounceAlgro(n,p,k,array,x,y)
            ans1 = naiveAlgro(n,p,k,array,x,y)
            if ans!=ans1:
                print(array,n,p,k,x,y,ans,ans1)
