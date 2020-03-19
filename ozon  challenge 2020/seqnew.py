import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    seq=input()
    n=len(seq)
    leftbra=[]
    rightbra=[]
    for i in range(n):
        if seq[i]=="(":
            leftbra.append(i)
        else:
            rightbra.append(i)
    rightbra.sort(reverse=True)
    lena,lenb=len(leftbra),len(rightbra)
    endres=min(lena,lenb)
    res=[]
    for i in range(endres):
        if leftbra[i]<rightbra[i]:
            res.append(leftbra[i])
            res.append(rightbra[i])
    res.sort()
    if len(res)==0:
        print(0)
    else:
        print(1)
        print(len(res))
        print(" ".join(str(x+1) for x in res))



