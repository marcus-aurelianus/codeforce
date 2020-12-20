import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def goodNum(num):
    strN = str(num)
    for ele in strN:
        if ele !='0' and num%(int(ele))!=0:
            return False
    return True

def gift():
    for _ in range(t):
        n = int(input())
        while True:
            if goodNum(n):
                break
            else:
                n+=1
        yield n
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])


#17214
