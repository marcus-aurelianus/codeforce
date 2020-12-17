import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input()) 
        commands = []
        for i in range(n):
            command = list(map(int,input().split()))
            commands.append(command)

        start = 0
        toReach = 0
        moving = False
        lastCommand = []
        lastStart = 0
        ans = 0
        for i in range(n):
            time, target = commands[i]
            if moving == False:
                moving = True
                lastStart=start
                lastCommand=commands[i]
                toReach = abs(target-start)+time
                start = target

            else:
                #print(toReach)
                if time>=toReach:
                    lastStart=start
                    lastCommand=commands[i]                    
                    toReach = abs(target-start)+time
                    start = target
                    ans+=1
                else:
                    
                    if lastStart>lastCommand[1]:
                        currPoint = lastStart-(time-lastCommand[0])
                    else:
                        currPoint = lastStart+(time-lastCommand[0])
                    #print(currPoint,target,lastStart,lastCommand)
                    if currPoint==target:
                        ans+=1

                        
        yield ans
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
