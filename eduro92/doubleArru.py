import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n, k, z = list(map(int,input().split()))
        arr = list(map(int,input().split()))
        if z==0:
            yield sum(arr[:k+1])
        else:
            plainsum=sum(arr[:k+1])
            maxsum=plainsum
            for i in range(1,k+1):
                maxtemp=plainsum
                tempsum=plainsum
                curepeat=arr[i]+arr[i-1]
                end=k

                times=z
                while end>i and times>0:
                    #print(end,i)
                    if end-i>=2:
                        tominus=arr[end]+arr[end-1]                        
                        tempsum+=(curepeat-tominus)
                        end-=2
                        maxtemp=max(maxtemp,tempsum)
                        times-=1
                    else:
                        inamo=arr[i-1]-arr[end]
                        tempsum+=(inamo)
                        end-=1
                        maxtemp=max(maxtemp,tempsum)
                        times-=1
                maxsum=max(maxsum,maxtemp)
                #print(i,maxsum)
            yield maxsum
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
 
