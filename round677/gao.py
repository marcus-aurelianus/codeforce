import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        num = int(input())
        books = list(map(int,input().split()))
        count = 0
        index = -1
        for i,ele in enumerate(books):
            if index>-1 and ele:
                count += (i-index-1)
            if ele:
                index = i
        yield count
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
