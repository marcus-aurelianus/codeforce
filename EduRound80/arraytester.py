a,b=[5,6]
import math
for i in range(1,7):
    for j in range(1,7):
        a,b=[i,j]
        apos,aposr=[],[]
        for i in range(1,a+1):
            apos.append([i])
            aposr.append([a+1-i])
        def getapos(lst,n):
            if len(lst[0])==b:
                return lst
            else:
                newlst=[]
                for ele in lst:
                    start=ele[-1]
                    for s in range(start,a+1):
                        newlst.append(ele+[s])
                return getapos(newlst,n-1)
        def getsporev(lst,n):
            if len(lst[0])==b:
                return lst
            else:
                newlst=[]
                for ele in lst:
                    start=ele[-1]
                    for s in range(1,start+1):
                        newlst.append(ele+[s])
                return getsporev(newlst,n-1)
        resa=getapos(apos,b)
        resb=getsporev(aposr,b)
        #print(len(resa),len(resb))
        #print(resa)
        #print(resb)
        def check(lst1,lst2):
            for i in range(b):
                if lst1[i]>lst2[i]:
                    return False
            return True
        res=0
        resarray=[]
        for elea in resa:
            for eleb in resb:
                if check(elea,eleb):
                    res+=1
                    resarray.append([elea,eleb])
        print(a,b,res,math.factorial(a+b*2-1)/math.factorial(a-1)//math.factorial(b*2))
        #print(resarray)
    
