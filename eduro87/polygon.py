import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
#3222211133
from math import tan,pi 
  
# Function to find the apothem 
# of a regular polygon 
def polyapothem(n, a): 
      
    # Side and side length cannot be negative 
    if (a < 0 and n < 0): 
        return -1
  
    # Degree converted to radians 
    return a / (2 * tan((180 / n) * 
                   pi / 180)) 
  

        
def gift():
    for _ in range(t):
        n = int(input())
        yield '{0:.12}'.format(2*polyapothem(n*2, 1))

            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
