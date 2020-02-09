def subsIns():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        if max(a)-min(a)>=n:
            yield 'YES'
            yield '1 '+str(n)
        else:
            found=0
            for i in range(n):
                for j in range(i+1,n+1):
                    newL=a[i:j]
                    if max(newL)-min(newL)>=j-i:
                        #print(newL,i,j)
                        found=1
                        yield 'YES'
                        yield str(i+1)+" "+str(j)
                    if found==1:
                        break
            if found==0:
                yield 'NO'
                
if __name__ == '__main__':      	
    t= int(input())
    ans = subsIns()
    print(*ans,sep='\n')
