import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(cou):
        a,b,t= [int(x) for x in input().split()]
        pattern=input()
        prev=pattern[-1]
        n=len(pattern)
        res=None
        prevpos=n
  
        if prev=="B":
            if (t>=b and pattern[n-2]=="B"):
                t-=b
                prevpos-=1
            elif (t>=a and pattern[n-2]=="A"):
                t-=a
                prevpos-=1
                prev=pattern[-2]
            else:
                res=n
        else:
            if (t>=a and pattern[n-2]=="A"):
                t-=a
                prevpos-=1
            elif (t>=b and pattern[n-2]=="B"):
                t-=b
                prevpos-=1
                prev=pattern[-2]
            else:
                res=n
        #print(pattern,res)
        if res:
            yield res
        else:
            for i in range(n-2):
                currpos=n-(i+3)
                currchar=pattern[currpos]
                #print(pattern,currpos,t,currchar)
                if currchar!=prev:
                    
                    if currchar=="A":
                        
                        if t>=a:
                           
                            t-=a
                            
                        else:
                            res=currpos+2
                            break
                    else:
                        if t>=b:
                            
                            t-=b
                        else:
                            res=currpos+2
                            break
                    prevpos=currpos+1
                    prev=currchar
                else:  
                    continue
            #print(pattern,res,prevpos)
            if res==None:
                yield 1
            else:

                    
                yield min(res,prevpos)
        #yield res,prevpos
                    
            
            
        
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
