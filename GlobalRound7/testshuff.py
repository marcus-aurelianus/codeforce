import random
def func1(string):
    n=len(string)
    if n==1:
        return string[0]
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
            return ans+ans[::-1]
            
        elif s==e:
            return ans+string[s]+ans[::-1]
            
        elif s==e-1:
            return ans+string[s]+ans[::-1]
            
        countsame=1
        for i in range(s+1,e+1):
            if string[i]==string[s]:
                countsame+=1
            else:
                break

        curr=string[s:s+countsame]
        mid=s+countsame
        currlen=countsame
        while mid+currlen<=e:
            tempcur=string[s:mid]
            #print(curr,tempcur,mid,string[mid:mid+currlen],tempcur==string[mid+1:mid+1+currlen][::-1])

                
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
        #print(curr,revcurr)
        if len1>=len2:
            return ans+curr+ans[::-1]
        else:
            return ans+revcurr+ans[::-1]
def func2(string):
    n=len(string)
    if n==1:
        print( string[0])
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
        
        sp,se=s,e
        prev=""
        while sp<=se:
            temprev=string[sp:se+1]
            if temprev==temprev[::-1]:
                prev=temprev
                break
            else:
                se-=1
        ep,ee=s,e
        end=""
        while ep<=ee:
            temprev=string[ep:ee+1]
            #print(temprev)
            if temprev==temprev[::-1]:
                end=temprev
                break
            else:
                ep+=1
        len1,len2=len(prev),len(end)
        if len1>=len2:
            return  ans+prev+ans[::-1]
        else:
            return ans+end+ans[::-1]

##for i in range(26):
##    for j in range(26):
##        print(i,j)
##        for k in range(26):
##            for l in range(26):
##                for m in range(26):
##                    string=chr(97+i)+chr(97+j)+chr(97+k)+chr(97+l)+chr(97+m)
##                    if func1(string)!=func2(string):
##                        print(string)

for i in range(10000):
    string=''
    for j in range(10):
        string+=chr(97+random.randrange(0,25))
    if func1(string)!=func2(string):
        print(string)
dic=['k','t','n','q','t','k']
res=['']
for i in range(8):
    temp=[]
    for j in range(6):
        for lis in res:
            kap=lis[:]
            kap+=dic[j]
            temp.append(kap)
    res=temp
for string in temp:
    if func1(string)!=func2(string):
        print(string)
