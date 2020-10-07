import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        array = list(map(int,input().split()))

        diff = 0
        for i in range(1,n):
            if array[i]>array[i-1]:
                diff+=1
        if k==1:
            if diff>0:
                yield -1
            else:
                yield 1
        elif diff==0:
            yield 1
        else:
            if diff%(k-1):
                yield diff//(k-1)+1
            else:
                yield diff//(k-1)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
