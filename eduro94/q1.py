import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n= int(input())
        string = input()
        ans=[]
        for i in range(n):
            ans.append(string[2*i])
        yield "".join(ans)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)





#3 2 3 3
