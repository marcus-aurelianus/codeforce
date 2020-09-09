import sys
 
n = int(input())

if n==1:
    print("! 1",flush = True)
else:
    arry = [0]*n
    pos = None

    start = 0
    end = 1

    quried = 1
    while quried<n:
        query = "? {} {}".format(start+1,end+1)
        print (query, flush = True)
        ans1 = int(input())
        query = "? {} {}".format(end+1,start+1)
        print (query, flush = True)
        ans2 = int(input())
        if ans1>ans2:
            arry[start]=ans1
            start = end
            end = (end+1)%n
        else:
            arry[end]=ans2
            end = (end+1)%n
        
        quried+=1
        
    if start == end:
        arry[start]=n
    else:
        query = "? {} {}".format(start+1,end+1)
        print (query, flush = True)
        ans1 = int(input())
        query = "? {} {}".format(end+1,start+1)
        print (query, flush = True)
        ans2 = int(input())
        #print(arry)
        if ans1>ans2:
            arry[start]=ans1
            arry[end]=n
        else:
            arry[end]=ans2
            arry[start]=n
    print ("!",*arry , flush = True)


