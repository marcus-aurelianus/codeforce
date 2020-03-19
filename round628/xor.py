import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


u,v=list(map(int,input().split()))
if u>v:
    print(-1)
elif u==v:
    if u==0:
        print(0)
    else:
        print(1)
        print(u)
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
