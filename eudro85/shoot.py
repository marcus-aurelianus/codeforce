import sys
input = sys.stdin.buffer.readline
def gift():
    for _ in range(t):
        n=int(input())
        inamo=[]
        for i in range(n):
            mosnteri= list(map(int,input().split()))
            inamo.append(mosnteri)
        dingding=[max(inamo[0][0]-inamo[n-1][1],0)]
        biu=dingding[0]
        for i in range(n-1):
            curr=inamo[i][1]
            nexmon=inamo[i+1][0]
            temp=max(nexmon-curr,0) 
            biu+=temp
            dingding.append(temp)

        jojo=float('inf')
        for i in range(n):
            jojo=min(jojo,inamo[i][0] +biu-dingding[i])
            
        yield jojo

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
