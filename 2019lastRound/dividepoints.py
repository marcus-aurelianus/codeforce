if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int,input().split())))
    dic = {}
    for point in points:
        x , y = point
        alpha = ( x + y ) % 2 
        if alpha not  in dic:
            dic[alpha]=[]
        dic[alpha].append([x,y])
    print(dic)

        
