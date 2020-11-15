import sys
 
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
 
                    # Update indices of
                    # the substring
                    firstVar = x
                    lastVar = x
 
            # For the remaining characters of b
            else:
                elementFound = 0
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
 
# Driver Code
if __name__ == '__main__':
     
    # Given two string
    a = "abb"
    b = "ab"
 
    l = minLength(a, b)
    if (l != sys.maxsize):
        print(l)
    else:
        print("Impossible")
