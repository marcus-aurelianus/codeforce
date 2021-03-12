def minScoreTriangulation(A):
    """
    :type A: List[int]
    :rtype: int
    """
    n = len(A)
    dp = [[0]*n for i in range(n)]
    for l in range(2, n):
        for left in range(0, n - l):
            right = left + l
            dp[left][right] = float("Inf")
            for k in range(left + 1, right):
                dp[left][right] = min(dp[left][right], dp[left][k] + dp[k][right] + A[left]*A[right]*A[k])
    print(dp)
    return dp[0][-1]
minScoreTriangulation([1,3,1,4,1,5])
