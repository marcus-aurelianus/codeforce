import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        string = input()
        ans = False


        for i in range(4):
            #print(string[:i+1]+string[n-1-(2-i):])
            if string[:i+1]+string[n-1-(2-i):]=='2020':
                ans=True
        if string[n-4:]=='2020':
            ans=True
        yield 'YES' if ans else 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
