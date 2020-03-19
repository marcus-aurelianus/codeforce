for m in range(2,10):
    for n in range(m,10):

        a,b=m,n
        res=[[]]
        ##for i in range(a):
        ##    maxnum=b-a+i+1
        ##    temp=[[maxnum,False]]
        ##    while True:
        ##        tempinamp=[]
        ##        if len(temp[0])==a:
        ##            break
        ##        else:
        ##            for thistemp in temp:
        ##                numarr,paried=thistemp
        ##                for j in range(maxnum-1):
        ##                    plusprv=[j+1]+numarr
        ##                    plusnex=numarr+[j+1]
        while len(res[0])<a:
            temp=[]
            for ele in res:
                for i in range(b):
                    cop=ele[:]
                    cop.append(i+1)
                    temp.append(cop)
            res=temp


        def checkmonoandpair(lst):
            maxnum=max(lst)
            pos=lst.index(maxnum)
            if pos==0 or pos==len(lst)-1:
                return False
            for i in range(pos-1):
                if lst[i]>=lst[i-1]:
                    return False
            for i in range(pos,len(lst)-1):
                 if lst[i]<=lst[i+1]:
                    return False       
            paired=0
            found=[]
            for ele in lst:
                if ele in found:
                    paired+=1
                else:
                    found.append(ele)
                if paired>1:
                    return False
            if paired==1:
                return True
            else:
                return False

        fres=[]
        for ele in res:   
            if checkmonoandpair(ele):
                fres.append(ele)
        print(a,b,len(fres))
