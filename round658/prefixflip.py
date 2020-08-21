import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())

        a=list(input())
        b=list(input())
        
        res=[]
        
        for i in range(n):
            #print(a)
            if i==n-1:
                if a[0]==b[0]:
                    continue
            if a[0]==b[n-1-i]:
                res.append(1)
                a[0]='1' if b[n-1-i] == '0' else '1'
            res.append(n-i)
     


        yield " ".join(str(x) for x in [len(res)]+res)
 


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 001011

# 111011
# 111011

# 000100
# 001000

# 101011

# 010100
# 001010



#101111
#010000
#000010


#110100
#001011

#011
#10100
#11100


#11111
#00011

#11011
#00000
