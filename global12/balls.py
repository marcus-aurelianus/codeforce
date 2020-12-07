import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        balls = []
        for i in range(n):
            ball = list(map(int,input().split()))
            balls.append(ball)
        ans = False
        for i in range(n):
            temAns = True
            for j in range(n):
                if j!=n:
                    if abs(balls[i][0]-balls[j][0])+abs(balls[i][1]-balls[j][1])>k:
                        temAns = False
                        break
            if temAns:
                ans = True
                break
                    
        yield 1 if ans else -1      


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
