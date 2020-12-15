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
        g = [0] * 3
        for i, r in enumerate(s):
            for j, c in enumerate(r):
                if c == 'X':
                    f[(i+j)%3] += 1
                elif c == 'O':
                    g[(i+j)%3] += 1

        # way to present
        # 0-1/2
        # 1-0/2 
        # 2-0/1
        rKey = min([1,2,3,5,6,7], key=lambda x: f[x%3]+g[x//3])
        for i, r in enumerate(s):
            for j, c in enumerate(r):
                if c == 'X' and (i + j) % 3 == rKey%3:
                    s[i][j] = 'O'
                elif c == 'O' and (i + j) % 3 == rKey//3:
                    s[i][j] = 'X'                
            yield ''.join(s[i])

            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

# 1 2 3 3 3
# 0 0 0 1
#"{} {} {}".format(maxele,minele,minele)
