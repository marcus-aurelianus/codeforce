import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n = int(input())
    *a, = [int(x) for x in input().split()]
    a.sort(reverse=True)
    longest=None
    other=[]
    for ele in a:
        ina=bin(ele)
        if longest==None:
            longest=ele
        else:
            if len(bin(ele))>len(bin(longest)):
                other+=[longest]
                longest=ele          
            elif bin(ele).count('1')>bin(longest).count('1'):
                other+=[longest]
                longest=ele
            else:
                other+=[ele]

    res=[longest]+other
    print(" ".join(str(x) for  x in res))

            
