import itertools
class Solution(object):
   def canConvert(self, str1, str2):
        if str1 == str2:
            return True
        lookup = {}
        for i, j in zip(str1, str2):
            if lookup.setdefault(i, j) != j:
                return False
        return len(set(str2)) < 26

ob = Solution()
print(ob.canConvert("qwertyuiopasdfghjklzxcvbnm", "qwertyuiopasdfghjklzxcvbnm"))
