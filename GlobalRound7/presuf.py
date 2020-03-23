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
                yield ans+prev+ans[::-1]
            else:
                yield ans+end+ans[::-1]
   
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
