import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import gc
gc.enable()
from itertools import combinations
import math
def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences

    return "".join(lcs_algo)


# Function to find the length of
# smallest substring of a having
# string b as a subsequence
def minLength(a, b):
     
    # Stores the characters present
    # in string b
    Char = {}
    for i in range(len(b)):
        Char[b[i]] = Char.get(b[i], 0) + 1
 
    # Find index of characters of a
    # that are also present in string b
    CharacterIndex = {}
 
    for i in range(len(a)):
        x = a[i]
 
        # If character is present in string b
        if (x in Char):
             
            # Store the index of character
            CharacterIndex[x] = CharacterIndex.get(x, [])
            CharacterIndex[x].append(i)
 
    l = sys.maxsize
 
    # Flag is used to check if
    # substring is possible
    while(True):
         
        # Assume that substring is
        # possible
        flag = 1
 
        firstVar = 0
        lastVar = 0
         
        # Stores first and last
        # indices of the substring
        # respectively
        for i in range(len(b)):
             
            # For first character of string b
            if (i == 0):
                 
                # If the first character of
                # b is not present in a
                if (b[i] not in CharacterIndex):
                    flag = 0
                    break
 
                # If the first character of b
                # is present in a
                else:
                    
                    x = CharacterIndex[b[i]][0]
 
                    # Remove the index from map
                    CharacterIndex[b[i]].remove(
                    CharacterIndex[b[i]][0])

                    if (len(CharacterIndex[b[i]])==0):
                        del CharacterIndex[b[i]]
                    # Update indices of
                    # the substring
                    firstVar = x
                    lastVar = x
 
            # For the remaining characters of b
            else:
                elementFound = 0
                if b[i] in CharacterIndex:
                    for e in CharacterIndex[b[i]]:
                        if (e > lastVar):
                             
                            # If index possible for
                            # current character
                            elementFound = 1
                            lastVar = e
                            break
                     
                if (elementFound == 0):
                     
                    # If no index is possible
                    flag = 0
                    break
                 
        if (flag == 0):
             
            # If no more substring
            # is possible
            break
 
        # Update the minimum length
        # of substring
        l = min(l, abs(lastVar - firstVar) + 1)
 
    # Return the result
    return l
m,n = list(map(int,input().split()))
S1 = input()
S2 = input()


ans = lcs_algo(S1, S2, m, n)
if (len(ans)==0):
    print(0)
else:
    maxAns = 2
    for x, y in combinations(range(len(ans) + 1), r = 2):
        e = ans[x:y]
        if len(e)>1:
            a = minLength(S1,e)
            b = minLength(S2,e)
            maxAns = max(4*len(e)-a-b,maxAns)
    print(maxAns)
