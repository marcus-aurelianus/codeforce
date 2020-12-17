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
        pipa = False
        for i in range(n):
            time, target = commands[i]
            if moving == False:
                moving = True
                lastStart=start
                lastCommand=commands[i]
                toReach = abs(target-start)+time
                start = target
                pipa=True
                if i==n-1:
                    ans+=1
            else:
                #print(toReach)
                if time>=toReach:
                    lastStart=start
                    lastCommand=commands[i]                    
                    toReach = abs(target-start)+time
                    start = target

                    if i==n-1:
                        ans+=1
                    if pipa:
                        ans+=1
                    pipa=True
                else:
                    pipa=False
                    if lastStart>lastCommand[1]:
                        diff = time-lastCommand[0]-(target-lastCommand[1])
                        currPoint = lastStart-(time-lastCommand[0])
                    else:
                        diff = time-lastCommand[0]-(lastCommand[1]-target)
                        currPoint = lastStart+(time-lastCommand[0])
                        
                    toSpendTime = abs(target-lastStart)+lastCommand[0]
                    if lastStart<=lastCommand[1]:
                        if currPoint<=target and target<=lastCommand[1]:
                            #print(toSpendTime,commands[i][0])
                            if (i<n-1 and toSpendTime<=commands[i+1][0]) or i==n-1:
                                ans+=1
                    else:
                        if currPoint>=target and target>=lastCommand[1]:
                            #print(toSpendTime,commands[i][0])
                            if (i<n-1 and toSpendTime<=commands[i+1][0]) or i==n-1:
                                ans+=1                        

                        
        yield ans
                        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 17
# 17 1
