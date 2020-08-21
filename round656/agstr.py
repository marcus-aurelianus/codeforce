import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math


def gift():
    for _ in range(t):
        n=int(input())
        arry= input()
        
        if n==1:
            if arry[0]=='a':
                yield 0
            else:
                yield 1
        else:
            def getminmove(array,lenit,char,type1):
                half=lenit//2
                
                if lenit==2 and type1==False:
                    return min(getminmove(array[:half],half,chr(ord(char)+1),True)+getminmove(array[half:],half,chr(ord(char)+2),True),getminmove(array[:half],half,chr(ord(char)+2),True)+getminmove(array[half:],half,chr(ord(char)+1),True))
                elif type1:
                    ans=0
                    for ele in array:
                        if ele!=char:
                            ans+=1
                    #print(array,char,type1,ans)       
                    return ans
                else:
                    return min(getminmove(array[:half],half,chr(ord(char)+1),True)+getminmove(array[half:],half,chr(ord(char)+1),False),
                               getminmove(array[:half],half,chr(ord(char)+1),False)+getminmove(array[half:],half,chr(ord(char)+1),True))
            res=getminmove(arry,n,chr(ord('a')-1),False)

            yield res

                    
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
