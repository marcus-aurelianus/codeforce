n=100

for i in range(10,n+1):
    for j in range(10,n+1):
        u,v=i,j
        print(u,v)
        if u>v:
            print(-1)
        elif u==v:
            if u%2==0:
                if u==0:
                    print(0)
                else:
                    num1=int(u&(u-1))

                    if num1==u or num1==0:
                        print(-1)
                    else:
                        print(2)
                        print(str(num1)+" "+str(u-num1))
            else:
                print(2)
                print("1 "+str(v-1))
        else:
            if u%2==0:
                if v%2==0:
                    num=(v-u)//2

                    num2=int(num&(u))
                    if not num2:
                        print(2)
                        print(str(u+num)+" "+str(num))
                    else:
                        print(3)
                        print(str(u)+" "+str(num)+" "+str(num))
                else:
                    print(-1)
            else:
                if v%2==0:
                    print(-1)
                else:
                    num=(v-u)//2
                    num2=int(num&(u))
                    if not num2:
                        print(2)
                        print(str(u+num)+" "+str(num))
                    else:
                        print(3)
                        print(str(u)+" "+str(num)+" "+str(num))
