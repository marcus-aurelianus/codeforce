import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n= int(input())
    array=list(map(int,input().split()))

    maxnow=array[0]
    ans=[array[0]]
    for i in range(n-1):
        tempmax=array[i+1]+maxnow
        if tempmax>maxnow:
            maxnow=tempmax
            ans.append(maxnow)
        else:
            ans.append(tempmax)
        
    print(" ".join(str(x) for x in ans))
            
