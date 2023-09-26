import sys
sys.setrecursionlimit(10**6)

def solution(target):
    darts = {50: 1}
    for i in range(1, 21):
        darts[i] = 1
    for i in list(range(22, 41, 2)) + list(range(21, 61, 3)):
        darts[i] = 0
    dp = {key:[1, val] for key, val in darts.items()}
    def memo(target):
        if target in dp:
            return dp[target]
        dp[target] = [float("inf"), 0]
        for key, val in darts.items():
            if key >= target: continue
            dart_num, sing_num = memo(target - key)
            if dp[target][0] > dart_num + 1 or (dp[target][0] == dart_num + 1 and dp[target][1] < sing_num + val):
                dp[target] = [dart_num + 1, sing_num + val]
        return dp[target]
    return memo(target)
