import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        charit=input()
        n=len(charit)

        ans=0
        cur=0
        pexist=False
        for i in range(n):
            if charit[i]=="-":
                if cur<0:
                    ans+=((i+1))
                else:
                    ans+=1
                cur-=1
                
            else:
                pexist=True
                if cur<0:
                    ans+=(i+1)
                    cur=1
                else:
                    ans+=1
                    cur+=1
            if i==n-1 and cur<0:
                ans+=(i+1)
                

            #print(i,ans)

        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
