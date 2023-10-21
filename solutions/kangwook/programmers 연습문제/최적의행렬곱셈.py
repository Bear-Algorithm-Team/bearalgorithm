def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[float("inf") if i != j else 0 for i in range(n)] for j in range(n)]
    
    for r in range(1, n):
        for c in range(n - r):
            i, j = c, r + c
            
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
            
    return dp[0][-1]
