import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        array = []
        for i in range(n):
            a = input()
            array.append(list(a))

        for i in range(n):
            for j in range(n):
                changed = False
                if j>0 and j<n-1:
                    left,right = array[i][j-1],array[i][j+1]

                    if left == right and left == array[i][j] and array[i][j]!='.':
                        if array[i][j]=='X':
                            array[i][j]='O'
                        else:
                            array[i][j]='X'
                        changed = True
                if not changed:
                    if i>0 and i<n-1:
                        up,down = array[i-1][j],array[i+1][j]
                        if up == down and up == array[i][j] and array[i][j]!='.':
                            if array[i][j]=='X':
                                array[i][j]='O'
                            else:
                                array[i][j]='X'
        for i in range(n):
            yield "".join(array[i])

            


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
