import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        string = input()
        n = len(string)
        moves=[]
        curr=0
        if string[0]=='1':
            curr+=1
        for i in range(1,n):
            if string[i]=='1':
                curr+=1
            else:
                if curr:
                    moves.append(curr)
                curr=0
        if curr:
            moves.append(curr)
        moves.sort(reverse=True)

        m=len(moves)
        if m==0:
            yield 0
        else:
            ans=0
            for i in range(0,m,2):
                ans+=moves[i]
            yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
