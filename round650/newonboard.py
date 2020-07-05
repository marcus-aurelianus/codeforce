import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import copy
def gift():
    for _ in range(t):
        array = list(input())
        m= int(input())
        nums = list(map(int,input().split()))

        list1=[0]*26

        for a in array:
            list1[ord(a)-97]+=1
        ans=[0]*m
        ind=25

        while max(nums)>=0:
            L=[]
            for i in range(m):
                if nums[i]==0:
                    L.append(i)
                    nums[i]-=1
            lenl=len(L)
            #print(list1,ind)
            while list1[ind]<lenl:
                ind-=1
            for l in L:
                ans[l]=ind
            ind-=1
            for l in L:
                for i in range(m):
                    nums[i]-=abs(i-l)

        yield ("".join([chr(a+97) for a in ans]))
                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
