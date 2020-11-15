import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        
        ans = list(range(1,n+1 ))
        yield n
        yield " ".join([str(x) for x in ans])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

#1+2
#"{} {} {}".format(maxele,minele,minele)
# 1 2 3 4
# 10 9 8 7

# 1 2 3 4

# 9 2 3 4
# 8 1 3 4
# 7 1 2 4
# 6 1 2 3

# 1 2 3
# 1 3 4
# 3 3 6
# 6 6 6
