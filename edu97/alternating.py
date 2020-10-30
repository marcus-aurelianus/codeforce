import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        inputString = input()
        zCont = 0
        oCont = 0
        for i in range(n-1):
            if (inputString[i]==inputString[i+1]):
                if inputString[i]=='0':
                    zCont += 1
                else:
                    oCont += 1
        yield max(zCont,oCont)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 180 x = 225 y

# 4x = 5y
 
