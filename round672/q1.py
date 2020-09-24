import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        ans = 'NO'
        for i in range(1,n):
            if arry[i]>=arry[i-1]:
                ans = 'YES'
                break 
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
