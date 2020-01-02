def subsIns():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        sum1=sum(a)
        xor=0
        for ele in a:
            xor^=ele
        if sum1==2*xor:
            yield 0
            yield ""
        elif xor==0:
            yield 1
            yield sum1
        else:
            yield 2
            yield str(xor)+" "+str(xor+sum1)
if __name__ == '__main__':
    t= int(input())
    ans = subsIns()
    print(*ans,sep='\n')
