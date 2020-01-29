import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



def prefix():
    for _ in range(t):
        n,x=map(int,input().split())
        #print(n,x)
        string=input()
        LtoR=0
        RtoL=0
        tempL,tempR=0,0
        maxL,maxR=0,0
        for i in range(n):
            if string[i]=='0':
                tempL+=1
            else:
                tempL-=1
            if tempL==0:
                LtoR+=1
            if string[n-i-1]=='0':
                tempR+=1
            else:
                tempR-=1
            if tempL==0:
                RtoL+=1
        sum01=tempL
        #print(sum01,x)
        if sum01==0:
            yield -1
        else:
            if (sum01>0 and x>0) or (sum01<0 and x<0):
                if sum01//x==0:
                    yield LtoR+RtoL+1
                else:
                    yield max(LtoR,RtoL)+1
            elif x==0:
                yield 1
            else:
                yield 0
                
        

if __name__ == '__main__':
    t= int(input())
    ans = prefix()
    print(*ans,sep='\n')
            
