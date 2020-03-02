import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__





def gift():
    for _ in range(cou):

        a,b= [int(x) for x in input().split()]
        if a==b:
            yield 0
        else:
            if b>a:
                if (abs(a-b))%2==0:
                    yield 2
                else:
                    yield 1
            else:
                if (abs(a-b))%2==0:
                    yield 1
                else:
                    yield 2

       
            

            
          
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
