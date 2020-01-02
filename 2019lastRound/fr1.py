def subsIns():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        if max(a)-min(a)>=n:
            yield 'YES'
            yield '1 '+str(n)
        else:
            found=0
            for i in range(n-1):
                if abs(a[i+1]-a[i])>=2:
                    found=1
                    yield 'YES'
                    yield str(i+1)+' '+str(i+2)
                    break
            if found==0:
                yield 'NO'
            
if __name__ == '__main__':
    t= int(input())
    ans = subsIns()
    print(*ans,sep='\n')
