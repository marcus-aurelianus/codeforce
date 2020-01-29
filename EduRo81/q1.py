import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

dic={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
dic1={1:2,7:3}

def maxnum():
    for _ in range(t):
        num=int(input())
        if num%2==0:
            x1=num//2
            res=int("".join(["1"]*x1))
        else:
            x1=(num-3)//2
            res=int("".join(["7"]+["1"]*x1))
        
        yield res
        

if __name__ == '__main__':
    t= int(input())
    ans = maxnum()
    print(*ans,sep='\n')
            
