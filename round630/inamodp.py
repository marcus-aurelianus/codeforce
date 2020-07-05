import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


        
    
if __name__ == '__main__':
    t= int(input())
    print("2 3")
    print(str(131072+t)+" "+str(t)+" "+str(131072))
    print(str(131072)+" "+str(131072+t)+" "+str(t))


