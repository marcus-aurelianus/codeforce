if __name__ == '__main__':
    n= int(input())
    lst=[]
    for i in range(n):
        lst.append([int(x) for x in input().split(" ")])
    for ele in lst:
        maxEle=max(ele)
        if sum(ele)-maxEle+1>=maxEle or sum(ele)-maxEle==0:
            print("YES")
        else:
            print("NO")
