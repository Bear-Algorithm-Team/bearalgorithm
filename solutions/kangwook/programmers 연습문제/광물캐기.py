def solution(picks, minerals):
    """
    
    dp[(dia, iron, stone)] = 곡괭이를 (dia, iron, stone)개 사용했을 때 최소 피로도
    
    """
    fatigue_table = [{"diamond":1, "iron":1, "stone": 1}, 
                     {"diamond":5, "iron":1, "stone": 1}, 
                     {"diamond":25, "iron":5, "stone": 1}]
    dp = {}
    picks = tuple(picks)
    def calc_fatigue(minerals, cur_pick):
        return sum(fatigue_table[cur_pick][mineral] for mineral in minerals)
    
    def dfs(minerals, cur_picks):
        if cur_picks in dp:
            return dp[cur_picks]
        if cur_picks > picks: 
            return float('inf')
        if sum(cur_picks) == sum(picks): 
            return 0

        j, k, l = cur_picks
        dp[cur_picks] = min(dfs(minerals[5:], (j + 1, k, l)) + calc_fatigue(minerals[: 5], 0), \
                            dfs(minerals[5:], (j, k + 1, l)) + calc_fatigue(minerals[: 5], 1), \
                            dfs(minerals[5:], (j, k, l + 1)) + calc_fatigue(minerals[: 5], 2))
        
        return dp[cur_picks]
    return dfs(minerals, (0, 0, 0))
