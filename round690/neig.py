import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        steps = 0
        while True:
            if len(array)==1:
                break
            elif len(array)==2:
                if array[0]!=array[1]:
                    steps+=1
                    break
                else:
                    break
            else:
                same = True
                for i in range(len(array)-1):
                    if array[i]!=array[i+1]:
                        same=False
                        break
                if same:
                    break
                else:
                    maxNum = max(array)
                    lenArray = len(array)
                    i = 0
                    #print(array)
                    changes = 0
                    while i<lenArray-1:
                        if array[i]<maxNum:
                            tem = array[i]+array[i+1]
                            array=array[:i]+[array[i]+array[i+1]]+array[i+2:]
                            lenArray = len(array)
                            steps+=1
                            changes+=1
                            #print(tem)
                            if tem>=maxNum:
                                i+=1
                        else:
                            i+=1
                    if changes == 0:
                        lenA = len(array)
                        if lenA>2:
                            array= array[:-2]+ [array[-1]+array[-2]]
                            steps+=1
                    #print(array)
        yield steps
                            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
    
# 5 1 2 4 5 1 6 4 2
