import random
from copy import deepcopy
def solve(n,m,arys):

    ans = []
    irange = []
    if m==2:
        j=0
        for i in range(n-1):
            x1 = arys[i][j]
            x2 = arys[i][j+1]
            x3 = arys[i+1][j]
            x4 = arys[i+1][j+1] 
            if i!=n-2:
                diu = []
                if x1+x2!=0:
                    if x1==1:
                        diu.append(i)
                        diu.append(j)
                    if x2==1:
                        diu.append(i)
                        diu.append(j+1)
                    if x1+x2==2:
                        diu.append(i+1)
                        diu.append(j)
                       
                    else:
                        diu.append(i+1)
                        diu.append(j)
                        diu.append(i+1)
                        diu.append(j+1) 
                    if (len(diu)!=0):
                        ans.append(diu)
                       
                        for z in range(3):
                            x = diu[z*2]
                            y = diu[z*2+1]
                            arys[x][y] = (1-arys[x][y])
            else:
                if sum([x1,x2,x3,x4])==4:
                    ans.append([i,j+1,i+1,j,i+1,j+1])
                    ans.append([i,j,i,j+1,i+1,j])
                    ans.append([i,j,i,j+1,i+1,j+1])
                    ans.append([i,j,i+1,j,i+1,j+1])
                    arys[i][j]=0
                    arys[i][j+1]=0
                    arys[i+1][j]=0
                    arys[i+1][j+1]=0
                elif sum([x1,x2,x3,x4])==0:
                    continue
                else:
                    while sum([x1,x2,x3,x4])!=0:
                        x1 = arys[i][j]
                        x2 = arys[i][j+1]
                        x3 = arys[i+1][j]
                        x4 = arys[i+1][j+1]
                        diu = []
                        #print(x1,x2,x3,x4)
                        if sum([x1,x2,x3,x4])==1:
                            if x1==1:
                                diu.extend([i,j])
                            elif x2==1:
                                diu.extend([i,j+1])
                            elif x3==1:
                                diu.extend([i+1,j])
                            else:
                                diu.extend([i+1,j+1])
                            if x1==0:
                                diu.extend([i,j])
                            if x2==0:
                                diu.extend([i,j+1])

                            if len(diu)==4:
                                if x3==0:
                                    diu.extend([i+1,j])
                                else:
                                    diu.extend([i+1,j+1])
                            elif len(diu)==2:
                                diu.extend([i+1,j])
                                diu.extend([i+1,j+1])
                        elif sum([x1,x2,x3,x4])==2:
                            if x1==0:
                                diu.extend([i,j])
                            if x2==0:
                                diu.extend([i,j+1])                                    
                            if x3==0:
                                diu.extend([i+1,j])
                            if x4==0:
                                diu.extend([i+1,j+1])
                            if x1==1:
                                diu.extend([i,j])
                            elif x2==1:
                                diu.extend([i,j+1]) 
                            elif x3==1:
                                diu.extend([i+1,j])
                            else:
                                diu.extend([i+1,j+1])
                        elif sum([x1,x2,x3,x4])==3:
                            if x1==1:
                                diu.extend([i,j])
                            if x2==1:
                                diu.extend([i,j+1])                                    
                            if x3==1:
                                diu.extend([i+1,j])
                            if x4==1:
                                diu.extend([i+1,j+1])                                
                        if (len(diu)>6):
                            print(sum([x1,x2,x3,x4]))
                            print(diu,'lat')
                        if (len(diu)!=0):
                            ans.append(diu)
                            for z in range(3):
                                x = diu[z*2]
                                y = diu[z*2+1]
                                arys[x][y] = (1-arys[x][y])
                
    else:   
        for kap in range(n//2):
            irange.append(kap*2)
        if n%2:
            irange.append(n-2)
        for i in irange:
            for j in range(m-1):
                x1 = arys[i][j]
                x2 = arys[i][j+1]
                x3 = arys[i+1][j]
                x4 = arys[i+1][j+1]
                if j!=m-2:
                    if sum([x1,x3])==0:
                        continue
                    else:
                        #print(x1,x2,x3,x4)
                        diu = []
                        if x1==1:
                           diu.append(i)
                           diu.append(j)
                        if x3==1:
                           diu.append(i+1)
                           diu.append(j)
                        if len(diu)==2:
                            diu.append(i)
                            diu.append(j+1)
                            diu.append(i+1)
                            diu.append(j+1)
                        else:
                            if x2==1:
                                diu.append(i)
                                diu.append(j+1)
                            if len(diu)==4:
                                diu.append(i+1)
                                diu.append(j+1)
                        ans.append(diu)
                        #print(diu)
##                        if (len(diu)!=6):
##                            print(sum([x1,x2,x3,x4]))
##                            print(diu,'ear')
                        for z in range(3):
                            x = diu[z*2]
                            y = diu[z*2+1]
                            arys[x][y] = (1-arys[x][y])
                else:
                    if sum([x1,x2,x3,x4])==4:
                        ans.append([i,j+1,i+1,j,i+1,j+1])
                        ans.append([i,j,i,j+1,i+1,j])
                        ans.append([i,j,i,j+1,i+1,j+1])
                        ans.append([i,j,i+1,j,i+1,j+1])
                        arys[i][j]=0
                        arys[i][j+1]=0
                        arys[i+1][j]=0
                        arys[i+1][j+1]=0
                    elif sum([x1,x2,x3,x4])==0:
                        continue
                    else:
                        while sum([x1,x2,x3,x4])!=0:
                            x1 = arys[i][j]
                            x2 = arys[i][j+1]
                            x3 = arys[i+1][j]
                            x4 = arys[i+1][j+1]
                            diu = []
                            #print(x1,x2,x3,x4)
                            if sum([x1,x2,x3,x4])==1:
                                if x1==1:
                                    diu.extend([i,j])
                                elif x2==1:
                                    diu.extend([i,j+1])
                                elif x3==1:
                                    diu.extend([i+1,j])
                                else:
                                    diu.extend([i+1,j+1])
                                if x1==0:
                                    diu.extend([i,j])
                                if x2==0:
                                    diu.extend([i,j+1])

                                if len(diu)==4:
                                    if x3==0:
                                        diu.extend([i+1,j])
                                    else:
                                        diu.extend([i+1,j+1])
                                elif len(diu)==2:
                                    diu.extend([i+1,j])
                                    diu.extend([i+1,j+1])
                            elif sum([x1,x2,x3,x4])==2:
                                if x1==0:
                                    diu.extend([i,j])
                                if x2==0:
                                    diu.extend([i,j+1])                                    
                                if x3==0:
                                    diu.extend([i+1,j])
                                if x4==0:
                                    diu.extend([i+1,j+1])
                                if x1==1:
                                    diu.extend([i,j])
                                elif x2==1:
                                    diu.extend([i,j+1]) 
                                elif x3==1:
                                    diu.extend([i+1,j])
                                else:
                                    diu.extend([i+1,j+1])
                            elif sum([x1,x2,x3,x4])==3:
                                if x1==1:
                                    diu.extend([i,j])
                                if x2==1:
                                    diu.extend([i,j+1])                                    
                                if x3==1:
                                    diu.extend([i+1,j])
                                if x4==1:
                                    diu.extend([i+1,j+1])                                
                            if (len(diu)>6):
                                print(sum([x1,x2,x3,x4]))
                                print(diu,'lat')
                            if (len(diu)!=0):
                                ans.append(diu)
                                for z in range(3):
                                    x = diu[z*2]
                                    y = diu[z*2+1]
                                    arys[x][y] = (1-arys[x][y])
                        
    
    return ans,arys

for x in range(2,10):
    for y in range(2,10):
        print(x,y)
        for rounds in range(10000):
            matrix = []
            for i in range(x):
                tem=[]
                for j in range(y):
                    tem.append(random.randint(0,1))
                matrix.append(tem)
            matrixCopy = deepcopy(matrix)
            ans,newMat = solve(x,y,matrix)
            bingo = True
            for ele in newMat:
                if not bingo:
                    break
                for e in ele:
                    if e!=0:
                        bingo = False
                        break
            
            if len(ans)>x*y or not bingo:
                print(ans,matrixCopy)
            
