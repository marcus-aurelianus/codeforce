import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        aabb = input()
        n = len(aabb)
        ans = n
        curB = 0
        for i in range(n):
            #print(i, curB,aabb[n-1-i])
            if aabb[n-1-i]=='B':
                curB += 1
            else:
                if curB>=1:
                    ans -= 2
                    curB -= 1
        ans -= (curB//2)*2
        yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
