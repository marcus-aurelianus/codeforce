
if __name__ == '__main__':
    n= int(input())
    gift = [int(x) for x in input().split()]
    res=[]
    last=0
    kappa = list(range(1,n+1))
    for i , x in  enumerate(gift):
        kappaTR=-1
        if x==0:
            nextZ= next((i for i, x in enumerate(gift[i+1:]) if x==0), None)
            if nextZ==None:
                res+=[0]
            else:
                kappaTR=nextZ+2+i
                while True:
                    if kappaTR in gift:
                        kappaTR-=1
                    else:
                        res+=[kappaTR]
                        break
            last=i
        else:
            res+=[x]
        if x in kappa:
            kappa.remove(x)
        if kappaTR in kappa:
                kappa.remove(kappaTR)
    res[last]=kappa[0]
    print(" ".join(str(x) for x in res))
    
    

