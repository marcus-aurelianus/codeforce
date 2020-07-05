import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import copy
def gift():
    for _ in range(t):
        array = input()
        n= int(input())
        nums = list(map(int,input().split()))

        alphs=list(array)
        alphs.sort()

        
        dicrino={}
        for i in range(n):
            if nums[i]:
                nmh=dicrino.get(nums[i],[])
                nmh.append(i)
                dicrino[nums[i]]=nmh
        m=len(array)
        
        for i in range(m-n+1):
            prevele=None
            dic=copy.deepcopy(dicrino)
            rem=list(range(n))
            ans=[[]]*n
            starelepos=m-1-i

            got = True
            for j in range(n):
                if nums[j]==0:
                    if not prevele:
                        prevele=alphs[starelepos]
                    if prevele and prevele!=alphs[starelepos]:
                        got=False
                        break
                    ans[j]=alphs[starelepos]
                    starelepos-=1
                    rem.remove(j)
                   
            if not got:
                continue
            filling=True
            while filling and rem:
                #print('se',ans,rem,dic,starelepos)
                filling=False
                notava=True
                for inamo in sorted(dic.keys()):
                    for j in dic[inamo]:

                        temp=0
                        target=nums[j]
                        for k in range(n):

                            if ans[k]:
                                #print(j,k,starelepos,target)
                                if ord(ans[k])>ord(alphs[starelepos]):
                                    temp+=abs(k-j)
                        #print("jtm",j,temp,rem)
                        if temp==target and j in rem:
                            ans[j]=alphs[starelepos]
                            starelepos-=1
                            filling=True
                            rem.remove(j)
                            dic[inamo].remove(j)
                            break
                if starelepos+1>=len(dic) and not filling:
                    filling=True
                    starelepos-=1
            print(ans)      
            if rem==[]:
                break
        #print(ans,rem)
                    
        yield "".join(str(x) for x in  ans)
                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
