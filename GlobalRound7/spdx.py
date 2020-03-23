qn = int(input())
 
for loop in range(qn):
 
    s = list(input())
    n = len(s)
 
    lastif = None
    
    for i in range((n+1)//2):
 
        if s[i] == s[-1-i]:
            continue
        else:
            lastif = i
            break
 
    if lastif == None:
        print ("".join(s))
        continue
 
    form = s[:lastif]
    back = s[n-lastif:]
 
    midsub = s[lastif:n-lastif]
    mid = [""]

    for i in midsub:
        mid.append(i)
        mid.append("")
 
    R = [None] * len(mid)
    i = 0
    j = 0
    print(mid)
    while i < len(mid):
        while i-j >= 0 and i+j < len(mid) and mid[i-j] == mid[i+j]:
            j+=1
        R[i] = j
 
        k = 1
        while i-k >= 0 and i+k < len(mid) and k+R[i-k] < j :
            R[i+k] = R[i-k]
            k+=1
        i += k
        j -= k
 
    maxind = 0
    for i in range(len(mid)):
 
        if ( i+1 == R[i] or R[i] == len(mid)-i) and R[maxind] < R[i]:
             maxind = i
 
    #print (mid,R)
    #print (maxind)
 
    for i in range(maxind - R[maxind] + 1 , maxind + R[maxind]):
        form.append(mid[i])
 
    ans = form + back
    print(R)
    print ("".join(ans))
