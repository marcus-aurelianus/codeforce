import sys
#from bisect import bisect_right
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

##def find_gt(a, x):
##    'Find leftmost value greater than x'
##    i = bisect_right(a, x)
##    if i != len(a):
##        return i
##    return len(a)

if __name__ == '__main__':
    n = int(input())
    teach = list(map(int,input().split()))
    stud = list(map(int,input().split()))
##    res=[teach[0]-stud[0]]
##    ans=0
##    for i in range(1,n):
##        num=teach[i]-stud[i]
##        pos = find_gt(res, num)
##        pos2 = find_gt(res,-num)
##        res=res[:pos]+[num]+res[pos:]
##        ans+=(i-pos2)
##        #print(res,ans)
##
    res=list(map(lambda x,y:x-y,teach,stud))
    res.sort()
    start,end=0,n-1
    ans=0
    while start<end:
        if res[start]+res[end]>0:
            ans+=(end-start)
            end-=1
        else:
            start+=1
    print(ans)

    
    
        

