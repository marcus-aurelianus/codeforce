##for i in range(100,201):
##    if i%7%10==i%10%7:
##        print(i,'ding')
##    print(i,i%7%10,i%10%7)
a,b=4,6
s,e=1,50
for i in range(s,e+1):
    if i%a%b==i%b%a:
        print(i,'ding')
    print(i,i%a%b,i%b%a)
