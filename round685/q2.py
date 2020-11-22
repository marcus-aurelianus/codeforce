import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,q = list(map(int,input().split()))
        string = input()
        for i in range(q):
            l,r = list(map(int,input().split()))

            s = 0
            s1 = l-1
            ans = False
            for j in range(l-1):
                if string[j]==string[l-1]:
                    ans = True
                    break
            for j in range(r,n):
                if string[j]==string[r-1]:
                    ans = True
                    break
            if ans:
                yield 'YES'
            else:
                yield 'NO'
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
