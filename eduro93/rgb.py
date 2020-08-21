import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


r, g, b = list(map(int,input().split()))
rarry = list(map(int,input().split()))
garry = list(map(int,input().split()))
barry = list(map(int,input().split()))

rarry.sort()
garry.sort()
barry.sort()
dic={0:rarry,1:garry,2:barry}
dic1={0:'r',1:'g',2:'b'}
ans=0
while ([r,g,b].count(0)<=1):
    #print(r,g,b)
    #print(rarry,garry,barry)
    if r and g and b:
        rb= rarry[-1]
        gb= garry[-1]
        bb= barry[-1]
        maxnum=max([r,g,b])
        minnum=min([r,g,b])
        midnum=sum([r,g,b])-maxnum-minnum

        maxnum1=max([rb,gb,bb])
        minnum1=min([rb,gb,bb])
        midnum1=sum([rb,gb,bb])-maxnum1-minnum1
        #print(maxnum1,minnum1,midnum1)
        if rb==gb==bb:
            index1=[r,g,b].index(maxnum)
            bigarry=dic[index1]

            if midnum==maxnum:
                midarry=dic[[r,g,b].index(midnum,index1+1)]
            else:
                midarry=dic[[r,g,b].index(midnum)]
          
            bx=bigarry.pop()
            mx=midarry.pop()
            r=len(rarry)
            g=len(garry)
            b=len(barry)
            ans+=bx*mx

        else:
            #print(dic)

            index1=[rb,gb,bb].index(maxnum1)
            bigarry=dic[index1]
            if midnum1==maxnum1:
                midarry=dic[[rb,gb,bb].index(midnum1,index1+1)]
            else:
                midarry=dic[[rb,gb,bb].index(midnum1)]

            #print(bigarry,midarry)
            bx=bigarry.pop()
            mx=midarry.pop()
            r=len(rarry)
            g=len(garry)
            b=len(barry)
            ans+=bx*mx
       
    elif r and g:
        rx=rarry.pop()
        gx=garry.pop()       
        ans+=rx*gx
        r-=1
        g-=1
    elif g and b:
        bx=barry.pop()
        gx=garry.pop()       
        ans+=bx*gx
        g-=1
        b-=1
    elif r and b:
        rx=rarry.pop()
        bx=barry.pop()       
        ans+=rx*bx
        r-=1
        b-=1
    #print('last',r,g,b) 
print(ans)


