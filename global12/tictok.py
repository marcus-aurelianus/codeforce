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

        rowsO = []
        colsO = []
        rowsX = []
        colsX = []
        for i in range(n):
            allO = True
            allX = True
            for j in range(n):
                if not allO and not allX:
                    break
                if array[i][j]=='O':
                    allX = False
                elif array[i][j]=='X':
                    allO = False
                else:
                    allX = False
                    allO = False
            if allO:
                rowsO.append(i)
            if allX:
                rowsX.append(i)
            allO = True
            allX = True
            for j in range(n):
                if not allO and not allX:
                    break
                if array[j][i]=='O':
                    allX = False
                elif array[j][i]=='X':
                    allO = False
                else:
                    allX = False
                    allO = False
            if allO:
                colsO.append(i)
            if allX:
                colsX.append(i)
        i = 0
        while i<max(len(colsO),len(rowsO)):
            if i<len(colsO) and i<len(rowsO):
                array[rowsO[i]][colsO[i]]='X'
            elif i<len(colsO):
                array[0][colsO[i]]='X'
            elif i<len(rowsO):
                array[rowsO[i]][0]='X'
            i += 1
        i = 0
        while i<max(len(colsX),len(rowsX)):
            if i<len(colsX) and i<len(rowsX):
                array[rowsX[i]][colsX[i]]='O'
            elif i<len(colsX):
                array[0][colsX[i]]='O'
            elif i<len(rowsX):
                array[rowsX[i]][0]='O'
            i+=1
        for i in range(n):
            yield "".join(array[i])

                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
