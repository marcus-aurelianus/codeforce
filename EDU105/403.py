def canCross(stones):
    def dfs(stones, curr, k, target):
        if curr == target:
            return True
        for i in range(-1,2):
            if curr + (k+i) in stones and k+i>0:
                ans = dfs(stones, curr + (k+i), k+i, target)
                if ans:
                    return True
        return False
    return dfs(set(stones),0,0,stones[-1])
print(canCross([0,2]))
