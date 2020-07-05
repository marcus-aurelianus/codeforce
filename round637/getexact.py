dic={"1110111":0,"0010010":1, "1011101":2, "1011011":3, "0111010":4, "1101011":5, "1101111":6, "1010010":7, "1111111":8, "1111011":9}

dic1={0:"1110111", 1:"0010010", 2:"1011101", 3:"1011011", 4:"0111010", 5:"1101011", 6:"1101111", 7:"1010010", 8:"1111111", 9:"1111011"}
ans={}
for i in range(10):
    tempdic={}
    for j in range(10):
        if i !=j:
            counter=0
            tans=True
            for k in range(7):
                inputi=dic1[i][k]
                respecti=dic1[j][k]
                if inputi=='1' :
                    if respecti=='0':
                        tans=False
                        break
                    else:
                        continue
                else:
                    if respecti=='1':
                        counter+=1
                    else:
                        continue
            if tans:
                tempdic[j]=counter
    ans[i]=tempdic
print(ans)
            
