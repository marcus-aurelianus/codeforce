import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



def gift():
    for _ in range(t):
        n = int(input())
        num=((n-1)//4+1)
        yield (n-num)*'9'+num*'8'
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 80000
