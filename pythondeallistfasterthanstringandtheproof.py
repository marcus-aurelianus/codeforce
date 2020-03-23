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

            s,e=0,n-1
            while s<e:
                if string[s]==string[e]:
                    s+=1
                    e-=1
                else:
                    break
            form=[string[:s]]
            back=[string[e+1:]]
            srem=string[s:e+1]
            #print(srem)
            mid = [""]

            for i in srem:
                mid.append(i)
                mid.append("")
         
            R = [None] * len(mid)
            i = 0
            j = 0
            #print(mid)
            while i < len(mid):
                while i-j >= 0 and i+j < len(mid) and mid[i-j] == mid[i+j]:
                    j+=1
                R[i] = j
         
                k = 1
                while i-k >= 0 and i+k < len(mid) and k+R[i-k] < j :
                    R[i+k] = R[i-k]
                    k+=1
                i += k
                j -= k
         
            maxind = 0
            for i in range(len(mid)):
         
                if ( i+1 == R[i] or R[i] == len(mid)-i) and R[maxind] < R[i]:
                     maxind = i
         
            #print (mid,R)
            #print (maxind)

            for i in range(maxind - R[maxind] + 1 , maxind + R[maxind]):
                form.append(mid[i])
            ans=form+back
            #print(form,back)                
            yield "".join(ans)

   
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
