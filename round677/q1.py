import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num = input()
        tsnum = int(num[0])
        lenNum = len(num)
        yield (tsnum-1)*(10)+lenNum*(lenNum+1)//2
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
