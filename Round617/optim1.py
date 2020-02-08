import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
dic={"L":[-1,0],"R":1,"U":2,"D":3}

def cashback():
    for _ in range(t):
        prevpath={(0,0):[0]}
        n = int(input())
        string=input()
        currloc=[0,0]
        mindis=float('Inf')
        startloc=None
        
        for i in range(n):
            
            x,y=currloc
            if string[i]=="L":
                currloc=[x-1,y]
            elif string[i]=="R":
                currloc=[x+1,y]
            elif string[i]=="U":
                currloc=[x,y+1]
            elif string[i]=="D":
                currloc=[x,y-1]
            x,y=currloc
            
            exist=prevpath.get((x,y),None)
            #print(currloc,string,exist,prevpath)
            if exist:
                if i+1-exist[-1]<mindis:
                    #print(mindis,i+1,exist[-1])
                    mindis=i+1-exist[-1]
                    startloc=exist[-1]+1
                prevpath[(x,y)]+=[i+1]    
            else:
                prevpath[(x,y)]=[i+1]
        if startloc:
            yield str(startloc)+" "+str(startloc+mindis-1)
        else:
            yield -1
            
         
        
            
                    
            
if __name__ == '__main__':
    t= int(input())
    ans = cashback()
    print(*ans,sep='\n')
