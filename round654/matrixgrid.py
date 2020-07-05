import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        perit=k//n
        rem=k%n
        ans=0
        if rem:
            ans=2

        anslst=[]
        for i in range(n):
            if i <rem:
                tempans='1'*(max(perit+1+i-n,0))+'0'*(i-max(perit+1+i-n,0))+'1'*(perit+1-max(perit+1+i-n,0))+'0'*(n-perit-i-1)
            else:
                tempans='1'*(max(perit+i-n,0))+'0'*(i-max(perit+i-n,0))+'1'*(perit-(max(perit+i-n,0)))+'0'*(n-perit-i)
            anslst.append(tempans)
                
        yield ans
        for  i in range(n):
            yield anslst[i]
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            




##4 3 3 3
##4 3 3 3
##
##14
### 10 15 0 25
##1 0 0 0 0
##0 1 0 0 0
##0 0 1 0 0
##0 0 0 1 0
##0 0 0 0 1
