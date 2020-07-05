import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from copy import deepcopy
def gift():
    for _ in range(t):
        n,k=list(map(int,input().split()))
        gifts=list(map(int,input().split()))
        friends=list(map(int,input().split()))

        gifts.sort()
        friends.sort()

        res=0
        curr=0
        equalfriendcount=0
        desiredgift=0
        calit=False


##        for i in range(k):
##            
##            fri=friends[i]
##            if desiredgift==0 or desiredgift==fri:
##                desiredgift=fri
##                equalfriendcount+=1
##            else:
##                equalfriendcount=1
##                desiredgift=fri
##            #print(i,desiredgift,"inamo")
##            if i==k-1:
##                calit=True
##            elif friends[i+1]!=desiredgift:
##                calit=True
##            
##            
##            if calit:
##                #print(res,equalfriendcount,desiredgift)
##                for j in range(equalfriendcount):
##                    #print(curr+j,curr+equalfriendcount*desiredgift-j-1)
##                    res+=(gifts[curr+j]+gifts[curr+equalfriendcount-1+(desiredgift-1)*(j+1)])
##                curr+=(equalfriendcount*desiredgift)
##                calit=False
        s,e=0,n-1

        rem=[]
        #print(friends,gifts)
        for ele in friends:
            if ele==1:
                res+=(gifts[e]*2)
                e-=1
            else:
                rem.append(ele)
        rem=rem[::-1]
        for ele in rem:
            res+=gifts[s]
            res+=gifts[e]
            s+=ele-1
            e-=1
        yield res
                    

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
