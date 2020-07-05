q = int(input())
 
for loop in range(q):
 
    n = int(input())
 
    t = list(map(int,input().split()))
 
    dic = {}
    for i in t:
        dic[i] = 1
 
    if len(dic) == 1:
        k = 1
        ans = [1] * n
    elif n % 2 == 0:
 
        k = 2
        ans = []
        for i in range(n):
            if i % 2 == 0:
                ans.append(1)
            else:
                ans.append(2)
 
    else:
 
        flag = 0
        ans = []
 
        for i in range(n):
 
            if flag == 0 and t[i-1] == t[i]:
                flag = 1
 
            ans.append( (i+flag) % 2 )
 
        if flag == 0:
            ans[-1] = 2
            k = 3
        else:
            k = 2
 
        for i in range(n):
            ans[i] += 1
 
    print (k)
    print (*ans)
