import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n = int(input())
    *a, = [int(x) for x in input().split()]
    a.sort(reverse=True)
    single=[]
    mul=[]
    zeros=[]
    res=[]
    if n>1:
        if a[n-1]==0:
            zeros+=[0]
        elif a[n-1]!=a[n-2]:
            single+=[a[n-1]]  
        else:
            mul+=[a[n-1]]
        if a[0]==0:
            zeros+=[0]
        elif a[0]!=a[1]:
            single+=[a[0]]       
        else:
            mul+=[a[0]]
    else:
        single+=[a[0]]
    for i in range(1,n-1):
        if a[i]==0:
            zeros+=[0]
        elif a[i]!=a[i+1] and a[i]!=a[i-1]:
            single+=[a[i]]
        else:
            mul+=[a[i]]

    res=single+mul+zeros
    print(" ".join(str(x) for  x in res))

            
