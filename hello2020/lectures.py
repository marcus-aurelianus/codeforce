def kappa(A,B,n):
    for i in range(n-1):
        for j in range(1,n):
            if max(int(A[i][0]),int(A[j][0]))<=min(int(A[i][1]),int(A[j][1])) and not max(int(B[i][0]),int(B[j][0]))<=min(int(B[i][1]),int(B[j][1])):
                return 'NO'
            if not max(int(A[i][0]),int(A[j][0]))<=min(int(A[i][1]),int(A[j][1])) and  max(int(B[i][0]),int(B[j][0]))<=min(int(B[i][1]),int(B[j][1])):                                                                         
                return 'NO'
    return 'YES'

if __name__ == '__main__':
    n = int(input())
    lectA=[]
    lectB=[]
    for i in range(n):
        classes=input().split()
        lectA.append(classes[0:2])
        lectB.append(classes[2:])
        
    res=kappa(lectA,lectB,n)
    print(res)
