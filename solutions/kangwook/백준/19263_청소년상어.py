# input = open("a.txt", "r").readline

from copy import deepcopy

dirs = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
space = []
fishes_dir = {}
for i in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().split())
    space.append([a0, a1, a2, a3])
    fishes_dir_cur_row = [b0, b1, b2, b3]
    for j in range(4):
        fishes_dir[space[i][j]] = fishes_dir_cur_row[j]

ans = 0
def dfs(cur_r, cur_c, prev_sum, space, fishes_dir):
    """
    
    cur_r, cur_c: 현재 상어가 도착한 칸. 상어가 여기 도착한 경우에 상어는 이 칸의 물고기를 먹고, 이 칸의 방향을 갖는다.
    prev_sum: 상어가 현재 칸에 도달하는 과정에서 여태 잡아먹은 물고기들의 번호 총 합
    space: 현재 공간의 상태
    fishes_dir: 모든 물고기의 현재 방향
    
    """

    space = deepcopy(space)
    fishes_dir = deepcopy(fishes_dir)

    cur_shark_dir = fishes_dir[space[cur_r][cur_c]] # 상어가 현재 칸의 물고기의 방향을 가져감
    sum_updated = prev_sum + space[cur_r][cur_c] # 새로운 누적합 계산
    space[cur_r][cur_c] = -1

    for cur_fish_n in range(1, 17):
        """
        
        1. cur_fish_n번 물고기는 현재 방향으로 한 칸 이동을 시도한다. 단, 그 방향에 상어가 있거나 벽이면 방향을 반시계로 계속 튼다. 한바퀴 돌아도 갈데 없으면 그냥 멈춘다.
        2. 돌다가 갈곳 발견하면, 그곳으로 간다. 거기 물고기가 있으면, 서로 위치를 맞바꾼다.
          - space: 물고기 번호 맞바꾸기
        
        """
        cur_fish_r, cur_fish_c = -1, -1
        for i in range(4):
            for j in range(4):
                if space[i][j] == cur_fish_n:
                    cur_fish_r, cur_fish_c = i, j
        if (cur_fish_r, cur_fish_c) == (-1, -1):
            continue
        cur_fish_dir = fishes_dir[cur_fish_n]
        for _ in range(8):
            nr, nc = cur_fish_r + dirs[cur_fish_dir][0], cur_fish_c + dirs[cur_fish_dir][1] # 현재 방향으로 물고기가 이동했을 때 위치
            if 0 <= nr < 4 and 0 <= nc < 4 and space[nr][nc] != -1: 
                fishes_dir[cur_fish_n] = cur_fish_dir
                space[cur_fish_r][cur_fish_c], space[nr][nc] = space[nr][nc], space[cur_fish_r][cur_fish_c]
                break
            cur_fish_dir = cur_fish_dir % 8 + 1 # 갈 곳 없으니까 물고기 방향 회전

    space[cur_r][cur_c] = 0 # 상어 이제 움직일 거니까 칸을 비워줌
    nr, nc = cur_r, cur_c
    for _ in range(4):
        nr += dirs[cur_shark_dir][0]
        nc += dirs[cur_shark_dir][1]
        if not(0 <= nr < 4 and 0 <= nc < 4): break
        if space[nr][nc] == 0: continue
        dfs(nr, nc, sum_updated, space, fishes_dir)

    global ans
    ans = max(ans, sum_updated)

dfs(0, 0, 0, space, fishes_dir)
print(ans)
