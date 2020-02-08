import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
dic={"L":0,"R":1,"U":2,"D":3}
def cashback():
    for _ in range(t):
        n = int(input())
        string=input()
        pattern=[0,0,0,0]
        start=1
        yieldtype=None
        templongstart=1
        for i in range(n-1):
            
            if string[i]=="L":
                if pattern[0]==0:
                   pattern[0]=1
                else:
                   pattern=[1,0,0,0]
                   start=i+1
                if string[i+1]=="R":
                    start=i+1
                    yieldtype=2
                    break
            elif string[i]=="R":
                if pattern[1]==0:
                   pattern[1]=1
                else:
                   pattern=[0,1,0,0]
                   start=i+1
                if string[i+1]=="L":
                    start=i+1
                    yieldtype=2
                    break
            elif string[i]=="U":
                if pattern[2]==0:
                   pattern[2]=1
                else:
                   pattern=[0,0,1,0]
                   start=i+1
                if string[i+1]=="D":
                    start=i+1
                    yieldtype=2
                    break
            elif string[i]=="D":
                if pattern[3]==0:
                   pattern[3]=1
                else:
                   pattern=[0,0,0,1]
                   start=i+1
                if string[i+1]=="U":
                    start=i+1
                    yieldtype=2
                    break
            #print(pattern,string)

            if sum(pattern)==4:
                yieldtype=4
                templongstart=start
          
  
        if sum(pattern)==3 and pattern[dic[string[n-1]]]==0:
            templongstart=start
            yieldtype=4
            
            
        if yieldtype==2:
            yield str(start)+" "+str(start+yieldtype-1)
        elif yieldtype==4:
            yield str(templongstart)+" "+str(templongstart+yieldtype-1)
        else:
            yield -1
            
                    
            
if __name__ == '__main__':
    t= int(input())
    ans = cashback()
    print(*ans,sep='\n')
