import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
n = int(input())
for i in range(n):
    f,t = list(map(int,input().split()))
    if f>t:
        print('NO')
    elif f==t:
        print('YES')
    else:
        if f&1==0 and t&1:
            print('NO')
        else:
            binf = bin(f)[2:]
            bint = bin(t)[2:]
            ans = 'YES'

            n = len(bint)
            binf = '0'*(n-len(binf))+ binf

            currSum = 0
            for i in range(n):
                if bint[n-i-1] == '1':
                    currSum += 1                    
                if binf[n-i-1] == '1':
                    currSum -= 1
                if currSum>0:
                    ans = 'NO'
                    break
            if bint.count('1')>binf.count('1'):
                print('NO')
            else:
                print(ans)


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
