def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    def dfs(cur_loc, cnt):
        """
        
        cur_loc[0]: 현재 이동시킬 플레이어의 현재 위치
        cur_loc[1]: 방금 전 턴에 이동한 플레이어의 현재 위치
        cnt: 현재 이동시킬 플레이어를 이동시키기 전까지 이동한 전체 턴 수.
             - cnt가 짝수: A 플레이어가 이동할 차례.
             - cnt가 홀수: B 플레이어가 이동할 차례.
             
        리턴값: 결과적으로 말단노드까지 도착해 게임이 끝났을 때, 전체 이동한 턴 수.
              - 리턴값이 홀수: A 플레이어 승리.
              - 리턴값이 짝수: B 플레이어 승리.
        
        """
        result_win, result_lose = float("inf"), 0

        cur_r, cur_c = cur_loc[0]
        board[cur_r][cur_c] = 0 # 일단 현재 플레이어가 이동할 칸이 있을 거라 전제하고 보드에서 현재 칸을 지워준다.
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = cur_r + dr, cur_c + dc
            if not(0 <= nr < n and 0 <= nc < m) or board[nr][nc] == 0: continue
            
            # 현재 위치에서 이동을 할 수 있고 이로써 상대편이 죽는다면, 현재 플레이어의 승리를 리턴한다.
            if cur_loc[0] == cur_loc[1]:
                board[cur_r][cur_c] = 1
                return cnt + 1
            
            result = dfs([cur_loc[1], [nr, nc]], cnt + 1)
            
            if result % 2 != cnt % 2: # 현재 이동하기로 한 녀석이 결국 이 선택으로 승리함
                result_win = min(result_win, result)
            else:
                result_lose = max(result_lose, result)

        board[cur_r][cur_c] = 1
        
        # 현재 플레이어가 승리하는 결과를 갖고 있다면 그걸, 아니라면 지는 결과를 리턴.
        if result_win != float("inf"):
            return result_win
        elif result_lose != 0:
            return result_lose

        # 현재 플레이어가 어떤 곳으로도 이동하지 못한다면, 상대 플레이어의 승리를 리턴한다.
        return cnt

    return dfs([aloc, bloc], 0)
