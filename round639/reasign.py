import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

#+2 +5 +8 +11 +14 +17
#2 7 15 26 40 57
#
#(3n+1)*n/2
#1.5*n^2+0.5*n-cards=0
#(-0.5+-(0.25+6cards)**0.5)/3
def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        dic={}
        ans='YES'
        for i in range(n):
            bobo=(i+(arry[i]%n))%n
            ina=dic.get(bobo,False)
            if ina:
                ans='NO'
                break
            else:
                dic[bobo]=True
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
