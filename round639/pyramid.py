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
        cards=int(input())
        simcar=cards
        ans=0
        while True:
            ina=(-0.5+(0.25+6*cards)**0.5)/3      
            if ina==int(ina):
                dida=ina
            else:
                dida=int(ina)
            if dida!=0:
                ans+=1
                cards-=((3*dida+1)*dida//2)
            else:
                break
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
