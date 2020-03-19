import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':

    n,h,l,r = list(map(int,input().split()))
    sche = list(map(int,input().split()))
    lis = [0]+[float("-inf")] * (h-1)
    for i in range(n):
        nlis = [float("-inf")] * h
        na=sche[i]
        for j in range(h):
            if l<=(na+j)%h<=r:
                nlis[(na+j)%h]= max(nlis[(na+j)%h],lis[j] + 1)
            else:
                nlis[(na+j)%h]= max(nlis[(na+j)%h],lis[j])
            if l<=(na+j-1)%h<=r:
                nlis[(na+j-1)%h]= max(nlis[(na+j-1)%h],lis[j] + 1)
            else:
                nlis[(na+j-1)%h]= max(nlis[(na+j-1)%h],lis[j])
            #print((na+j)%h,(na+j-1)%h,nlis,lis)
        lis=nlis
            
    print (max(0,max(lis)))
    
    
        

