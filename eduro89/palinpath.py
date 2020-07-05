import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m= list(map(int,input().split()))
        
        if n<=m:
            seq=[]
            for i in range(n):
                tisrow=list(map(int,input().split()))
                seq.append(tisrow)
        else:
            seq=[]
            for j in range(m):
                seq.append([])
            for i in range(n):
                tisrow=list(map(int,input().split()))
                for j in range(m):
                    seq[j].append(tisrow[j])
            n,m=m,n
        #print(seq)
        basenum=((n+m)-1)//2
        oddcheck=((n+m)-1)%2
        totcheck=basenum+oddcheck
        ans=0
        for  i in range(totcheck):
            if i==basenum:
                continue
            else:
                farray=[]
                barray=[]
                spoint=[0,i]
                epoint=[n-1,m-1-i]
                if i<n:
                    roundlen=i+1
                    
                else:
                    roundlen=n

                for j in range(roundlen):
                    
                    s,e=spoint
                    
                    farray.append(seq[s][e])
                    spoint=[s+1,e-1]

                    s1,e1=epoint
                    #print(s1,e1,roundlen)
                    barray.append(seq[s1][e1])
                    epoint=[s1-1,e1+1]
                c1=0
                c0=0
                for ele in farray:
                    if ele:
                        c1+=1
                    else:
                        c0+=1
                for ele in barray:
                    if ele:
                        c1+=1
                    else:
                        c0+=1
                if c1==0 or c0==0:
                    continue
                else:
                    ans+=min(c1,c0)
        yield ans
                    

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


# 2x+y<a
# 2y+x<b

#3x+3y<a+b
#x<
            
