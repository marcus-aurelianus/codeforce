def subString(s): 
    # Pick starting point in outer loop 
    # and lengths of different strings for 
    # a given starting point
    res=0
    n=len(s)
    for i in range(n): 
        for len1 in range(i+1,n+1):
            tempstr=s[i: len1]
            if '1' in tempstr:
                temp=len(tempstr)%(tempstr.count('1'))
                if temp==0:
                    res+=1
    return res
  
if __name__ == '__main__':
    strR=input()
    print(subString(strR))
  
