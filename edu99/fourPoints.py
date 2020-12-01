import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        points = []
        sumX,sumY = 0,0
        for i in range(4):
            x,y = list(map(int,input().split()))
            sumX += x
            sumY += y
            points.append([x,y])

        yield sumX/4, sumY/4
        
                        
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
