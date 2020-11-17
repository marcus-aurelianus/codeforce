import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,c0,c1,h = list(map(int,input().split()))
        string = input()
        count0 = 0
        count1 = 0
        for ele in string:
            if ele=='0':
                count0+=1
            else:
                count1+=1
        yield min(c0,h+c1)*count0+min(c1,h+c0)*count1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
