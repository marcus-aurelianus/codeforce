import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        s = []
        for i in range(n):
            array = list(input())
            s.append(array)
        f = [0] * 3
        for i, r in enumerate(s):
            for j, c in enumerate(r):
                if c == 'X':
                    f[(i+j)%3] += 1
        rKey = min(range(3), key=lambda x: f[x])
        for i, r in enumerate(s):
            for j, c in enumerate(r):
                if c == 'X' and (i + j) % 3 == rKey:
                    s[i][j] = 'O'
            yield ''.join(s[i])

            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

# 1 2 3 3 3
# 0 0 0 1
#"{} {} {}".format(maxele,minele,minele)
