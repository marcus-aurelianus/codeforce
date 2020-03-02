for i in range(5):
    for j in range(5):
        for k in range(5):
            lst=[i,j,k]
            minx=min(lst)
            maxx=max(lst)
            sumx=sum(lst)
            midx=sumx-maxx-minx
            print(lst)
            if minx>=4:
                print (7)
            elif minx==3:
                print (6)
            elif minx==2:
                if maxx>=3:
                    print (5)
                else:
                    print (4)
            elif minx==1:
                if maxx>=2:
                    if midx>=2:
                        print (4)
                    else:
                        print (3)
                else:
                    print (3)
            else:
                if maxx>=2:
                    if midx>=2:
                        print (3)
                    else:
                        print (2)
                elif maxx==1:
                    if midx==1:
                        print (2)
                    else:
                        print (1)
                else:
                    print (0)



            
