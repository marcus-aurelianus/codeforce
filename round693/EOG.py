import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        eles = list(map(int,input().split()))
        eles.sort(reverse=True)

        bob = 0
        alice = 0
        for i in range(n):
            if i%2==0:
                if eles[i]%2==0:
                    alice+=eles[i]
            else:
                if eles[i]%2:
                    bob+=eles[i]
        if bob>alice:
            yield 'Bob'
        elif alice>bob:
            yield 'Alice'
        else:
            yield 'Tie'
                
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
