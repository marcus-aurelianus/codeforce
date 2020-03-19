import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    n=int(input())
    brackets=input()

    lefstk=[]
    rigstk=[]
    for i,bra in enumerate(brackets):
        if bra=="(":
            lefstk.append(i)
        else:
            rigstk.append(i)
    print("(",lefstk)
    print(")",rigstk)
    end=0
    if len(lefstk)!=len(rigstk):
        print(-1)
    else:
        for i in range(n//2):
            if i!=0:
                if rigstk[i]<rigstk[i-1]:
                    rigstk[i],rigstk[i-1]=rigstk[i-1],rigstk[i]
            print(lefstk[i],rigstk[i])
            if lefstk[i]>rigstk[i]:
                lefstk[i],rigstk[i]=rigstk[i],lefstk[i]
                end+=(abs(lefstk[i]-rigstk[i])+1)

    res=""
    for i in range(n):
        if i in lefstk:
            res+="("
        else:
            res+=")"
    print(res)
    print(end)
