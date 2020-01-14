def findYear():
    for _ in range(t):
        year = int(input())
        yield(lst1[(year-1)%n]+lst2[(year-1)%m])

if __name__ == '__main__':
    n,m=map(int,input().split())
    lst1=[ele for ele in input().split()]
    lst2=[ele for ele in input().split()]
    t= int(input())
    ans = findYear()
    print(*ans,sep='\n')
