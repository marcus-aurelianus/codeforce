import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num=int(input())
        for i in range(1,30):
            temp=int('1'*i,2)
            #print(temp,num%temp)
            if num%temp==0:
                
                rem=num//temp
                if temp!=1:
                    yield rem
                    break
                else:
                    if (rem+1)&rem==0:
                        yield temp
                        break
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
