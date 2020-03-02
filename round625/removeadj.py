import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


if __name__ == '__main__':
    t= int(input())
    word=input()
    res=0
    while True:
        n=len(word)
        toremove=[]

        if n==1:
            break
        for i in range(n):
            #print(toremove,ord(word[i]))
            if i==0:
                if ord(word[i])==ord(word[i+1])+1:
                    
                    if not toremove or  toremove[-1]!=i:
                       
  
                        toremove.append(i)
            elif i==n-1:
                if ord(word[i])==ord(word[i-1])+1:
                    
                    if not toremove or  toremove[-1]!=i:
                        

                        toremove.append(i)
            else:
                if ord(word[i])==ord(word[i+1])+1 or ord(word[i])==ord(word[i-1])+1:

                    if not toremove or  toremove[-1]!=i:
                  
                        toremove.append(i)
        
        res+=len(toremove)
        if not toremove:
            break
        counter=0
        for i in toremove:
            
            word=word[:(i-counter)]+word[(i-counter)+1:]
            counter+=1
            #print(word)
        print(toremove,word)
    print(res)

            

                    
                
        
            
        

            
