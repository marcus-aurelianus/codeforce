import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string=input()
        n=len(string)
        if n==1:
            yield string[0]
        else:
            ans=""
            s,e=0,n-1
            while s<e:
                if string[s]==string[e]:
                    ans+=string[s]
                    s+=1
                    e-=1
                else:
                    break
            
            if s>e:
                yield ans+ans[::-1]
                continue
            elif s==e:
                yield ans+string[s]+ans[::-1]
                continue
            elif s==e-1:
                yield ans+string[s]+ans[::-1]
                continue
            countsame=1
            for i in range(s+1,e+1):
                if string[i]==string[s]:
                    countsame+=1
                else:
                    break

            curr=string[s:s+countsame]
            mid=s+countsame
            currlen=countsame
            while mid+currlen<=e+1:
                tempcur=string[s:mid]
                temcurs=string[s:mid]
                print(curr,tempcur,mid,string[mid:mid+currlen],tempcur==string[mid+1:mid+1+currlen][::-1])

                    
                if tempcur==string[mid+1:mid+1+currlen][::-1]:
                    #print(curr,1)
                    curr=string[s:mid+currlen+1]
                    mid=mid+currlen
                    currlen=mid-s
                elif tempcur==string[mid:mid+currlen][::-1]:
                    #print(curr,2)
                    curr=string[s:mid+currlen]
                    mid+=currlen
                    currlen=mid-s
                else:
                    mid+=1
                    currlen+=1
                print(mid,currlen)
            revcountsame=1
            for i in range(1,e-s+1):
                #print(e,e-i,string[e-i],string[e])
                if string[e-i]==string[e]:
                    revcountsame+=1
                else:
                    break

            revcurr=string[e-revcountsame+1:e+1]
            mid=e-revcountsame
            currlen=revcountsame
            #print(revcurr,mid,currlen)
            while mid-currlen>=s:
                tempcur=string[mid+1:e+1]
                #print(tempcur,string[mid-currlen:mid],string[mid-currlen:e+1])

                if tempcur==string[mid-currlen:mid][::-1]:
                    #print(tempcur,string[mid-currlen:mid],2)
                    revcurr=string[mid-currlen:e+1]
                    mid-=currlen
                    currlen=e-mid
                elif tempcur==string[mid-currlen+1:mid+1][::-1]:
                    #print(tempcur,string[mid-currlen+1:mid+1],1)
                    revcurr=string[mid-currlen+1:e+1]
                    mid-=currlen
                    currlen=e-mid 
                else:
                    mid-=1
                    currlen+=1
                #print(revcurr )
            len1,len2=len(curr),len(revcurr)
            print(curr,revcurr)
            if len1>=len2:
                yield ans+curr+ans[::-1]
            else:
                yield ans+revcurr+ans[::-1]

   
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
