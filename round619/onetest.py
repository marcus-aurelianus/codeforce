for kap in range(2,20):
    for bobo in range(1,kap+1):

        n,m=kap,bobo


        o=n-m

        res=['0','1']


        #for ele in res:
            #print(ele,1)
        for i in range(n-1):
            temp=[]
            for ele in res:
                if ele.count('0')<o:
                    ina=ele+'0'
                    temp.append(ina)
                if ele.count('1')<m:
                    ina=ele+'1'
                    temp.append(ina)
            res=temp

        #print(len(res))

        maxres=0
        typeyo=None
        for ele in res:
            counter=0
            subs = [ele[i: j] for i in range(len(ele)) 
                  for j in range(i + 1, len(ele) + 1)]
            for sub in subs:
                if '1' in sub:
                    counter+=1
            if counter>maxres:
                typeyo=ele
                maxres=counter
        print(n,m,maxres,typeyo)
