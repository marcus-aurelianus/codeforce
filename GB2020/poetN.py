import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        string = input()
        n = len(string)
        if n==1:
            yield 0
        else:
            ans = 0
            start = 1
            solvedPos = defaultdict(lambda:False)
            while start<n:
                left,self = string[start-1],string[start]
                if start<n-1:
                    right = string[start+1]
                    

                if self==left:
                    if solvedPos[start]==False and solvedPos[start-1]==False:
                        solvedPos[start]=True
                        ans+=1

                if start<n-1 and left==right:
                    if solvedPos[start+1]==False and solvedPos[start-1]==False:
                        solvedPos[start+1]=True
                        ans+=1

                start+=1
            yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
# baebdcb
