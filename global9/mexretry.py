tt = int(input())
 
for loop in range(tt):
    
    n = int(input())
    a = list(map(int,input().split()))
    ans = []
    
    mexlis = [-1] * (n+1)
    for i in range(n):
        if a[i] <= n+1:
            mexlis[a[i]] = 0
 
    cnt = 0
    while True:
 
        for i in range(n+1):
            if mexlis[i] != cnt:
                mex = i
                break
 
        #print (*a,mex)
 
        if mex == n:
            for i in range(n):
                if a[i] != i:
                    ans.append(i+1)
                    a[i] = mex
                    break
            else:
                break
 
        else:
            ans.append(mex+1)
            a[mex] = mex
 
        cnt += 1
        for i in range(n):
            mexlis[a[i]] = cnt
 
 
    print (len(ans))
    print (*ans)
            
