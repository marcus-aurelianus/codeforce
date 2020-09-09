import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        overthere = 0
        ans = 0
        for i in range(n):
            if arry[i]<0:
                if overthere == 0:
                    ans += (-arry[i])
                else:
                    if overthere+arry[i]<0:
                        ans += -(overthere+arry[i])
                        overthere =0
                    else:
                        overthere+=arry[i]
                    
            else:
                overthere += arry[i]
        yield ans
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
