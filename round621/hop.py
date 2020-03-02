import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def hop():
    for _ in range(t):
        n,dis = [int(x) for x in input().split()]
        *a, = [int(x) for x in input().split()]
        a.sort()


        biggest=float("inf")
        for i in range(n):
            #print(biggest)
            rem=dis%a[n-i-1]
            quo=dis//a[n-i-1]
            #las1=((dis-(quo-1)*a[n-i-1])**2-a[n-i-1]**2)**0.5
            if rem==0:
                biggest=min(quo,biggest)

            else:
                if rem!=dis:
                    biggest=min(biggest,quo+1)

                else:

                    biggest=min(biggest,quo+2)
        yield biggest
         
        

if __name__ == '__main__':
    t= int(input())
    ans = hop()
    print(*ans,sep='\n')
            
