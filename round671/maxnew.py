import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        start = 1
        acum = 0
        ans = 0
        while True:
            tis = (start+1)*start//2
            if tis + acum <= n:
                acum += tis
                ans += 1
                start += 2**ans
            else:
                break
        yield ans
                        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
