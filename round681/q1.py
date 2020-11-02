import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        ans = []
        for i in range(n):
            ans.append(n*4-(i+1)*2)
        yield " ".join(str(x) for x in ans)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 5
# 18 14 12 10 8
