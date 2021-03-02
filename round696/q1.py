import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        b = input()
        a = []
        prev = 0
        for ele in b:
            curr = int(ele)
            if curr+1 == prev:
                a.append('0')
                prev = curr + 0
            else:
                a.append('1')
                prev = curr + 1
        yield "".join(a)
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
