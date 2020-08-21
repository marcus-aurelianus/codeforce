import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())

        s1=list(input())
        s2=list(input())
        
        res=[]
        last = s1[0]
        for i in range(1, n):
            #print(a)
            if s1[i] != last:
                res.append(i)
                last = s1[i]
        for i in range(n - 1, -1, -1):
            #print(a)
            if s2[i] != last:
                res.append(i + 1)
                last = s2[i]        
     


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
