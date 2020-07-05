import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        candies=list(map(int,input().split()))
        s,e=0,n-1
        alice=0
        aeaten=0
        bob=0
        beaten=0
        roundkap=0
        temp=0
        while s<=e:
            if s==e:
                if roundkap%2==0:
                    temp+=candies[s]
                    alice+=temp
                    roundkap+=1
                    break
                else:
                    temp+=candies[e]
                    bob+=temp
                    roundkap+=1
                    break
            else:
                if roundkap%2==0:
                    if temp==0:
                        temp=candies[s]
                    else:
                        temp+=candies[s]
                    if temp>beaten:
                        roundkap+=1
                        aeaten=temp
                        temp=0
                        alice+=aeaten
                    s+=1
                else:
                    if temp==0:
                        temp=candies[e]
                    else:
                        temp+=candies[e]
                    if temp>aeaten:
                        roundkap+=1
                        beaten=temp
                        temp=0
                        bob+=beaten
                    e-=1

        yield str(roundkap)+" "+str(alice)+" "+str(bob)            
                
                
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')



##100 55
##1 3 5
##33  22

##x+3*(k-x)=n
##n=3*k-2*x
##x=(3*k-n)//2
##1 3 1 3 1 3 49
            
