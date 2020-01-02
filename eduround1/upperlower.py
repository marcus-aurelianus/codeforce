if __name__ == '__main__':
    n,k,l= [int(x) for x in input().split(" ")]
    stringMap = [x.isupper() for  x in input()]
    ctn_T=stringMap.count(True)
    ctn_F=n-ctn_T
    ctn = True if ctn_T<ctn_F else False
    len_list=[]
    temp=None
    for i in range(n):
        if stringMap[i]==ctn:
            if temp==None:
                temp=i
            else:
                len_list.append(i-temp)
                temp=i

    ctn_show=min(ctn_T,ctn_F)
    for ele in len_list:
        if ele<l:
            ctn_show-=2
    print(max(ctn_show,0))
