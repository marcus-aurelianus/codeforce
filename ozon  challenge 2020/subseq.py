import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    seq=input()
    endans=[]
    while True:
        leftbra=[]
        rightbra=[]
        n=len(seq)
        print(seq)
        for i in range(n//2+(n%2)):
            if i==n//2+1:
                if seq[n-i-1]==")":
                    lena,lenb=len(leftbra),len(rightbra)
                    if lena>lenb:
                        rightbra.append(n-i-1)  
            else:
                if seq[i]=="(":
                    leftbra.append(i)
                if seq[n-i-1]==")":
                    rightbra.append(n-i-1)
        lena,lenb=len(leftbra),len(rightbra)
        endlen=(min(lena,lenb))
        ans=[]
        for i in range(endlen):
            ans.append(leftbra[i])
            ans.append(rightbra[i])
        ans.sort()
        if endlen==0:
            break
        else:
            #print(ans)
            counter=0
            for pos in ans:
                seq=seq[:(pos-counter)]+seq[(pos-counter+1):]
                counter+=1
            endans.append(ans)
    print(len(endans))
    for eachans in endans:
        print(len(eachans))
        print(" ".join(str(x+1) for x in eachans))


