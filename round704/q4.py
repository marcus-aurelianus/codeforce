import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
 
a,b,k = list(map(int,input().split()))


if a==0:
    if k==0:
        print ("Yes")
        print ("1"*b + "0"*a)
        print ("1"*b + "0"*a) 
    else:
        print('No')
elif k>a:
    if k>a+b:
        print('No')
    else:    
        ans1 = b*'1'+a*'0'
        ans2 = (a+b-k-1)*'1'+'0'+(k-a)*'1'+(a-1)*'0'+'1'
        if ans1[0]=='1' and ans2[0]=='1':
            print('Yes')
            print(ans1)
            print(ans2)
        else:
            print('No')
elif k==0:
    print ("Yes")
    print ("1"*b + "0"*a)
    print ("1"*b + "0"*a)    
elif k>0 and b==0:
    print('No')
else:
    
    ans1 = (b-1)*'1'+(a-k)*'0'+'1'+'0'*k
    ans2 = (b-1)*'1'+(a-k)*'0'+'0'*k + '1'
    if ans1[0] == '0' or ans2[0]=='0':
        print('No')
    else:
        print('Yes')
        print(ans1)
        print(ans2)
