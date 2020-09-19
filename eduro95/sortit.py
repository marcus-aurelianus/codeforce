import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
        pos = list(map(int,input().split()))

        unlocked = []
        unlockedval = []
        for i in range(n):
            if pos[i]==0:
                unlocked.append(i)
                unlockedval.append(array[i])
        unlockedval.sort(reverse=True)
        for i in range(len(unlocked)):
            array[unlocked[i]]=unlockedval[i]
        yield " ".join([str(x) for x in array])
        

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
