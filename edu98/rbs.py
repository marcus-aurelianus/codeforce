import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        s = input()
        l1 = 0
        l2 = 0
        ansL = 0
        for e in s:
            if e=="(":
                l1+=1
            elif e==")":
                if l1>=1:
                    l1-=1
                    ansL+=1
            elif e=="[":
                l2+=1
            elif e=="]":
                if l2>=1:
                    l2-=1
                    ansL+=1
        n = len(s)
        l1 = 0
        l2 = 0
        ansR = 0        
        for i in range(n):
            e = s[n-i-1]
            if e==")":
                l1+=1
            elif e=="(":
                if l1>=1:
                    l1-=1
                    ansR+=1
            elif e=="]":
                l2+=1
            elif e=="[":
                if l2>=1:
                    l2-=1
                    ansR+=1
        yield max(ansR,ansL)
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
