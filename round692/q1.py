import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        string = input()
        kap = 0
        for i in range(n):
            if string[n-1-i]==")":
                kap+=1
            else:
                break
        if kap>n-kap:
            yield 'Yes'
        else:
            yield 'No'
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
