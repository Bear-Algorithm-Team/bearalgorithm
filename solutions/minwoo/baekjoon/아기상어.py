from collections import deque

def bfs(i,j):
    visit = [[0]*n for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    q = deque()
    q.append([i,j])
    visit[i][j] = 1

    fish_pos = []
    while q :
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]

            if 0<=ny<n and 0<=nx<n and visit[ny][nx] == 0 and grid[ny][nx] <=shark_size:
                q.append([ny,nx])
                visit[ny][nx] = 1
                dp[ny][nx] = dp[y][x] + 1
                if 0 < grid[ny][nx] < shark_size : # 먹을 수 있는 물고기
                    fish_pos.append([dp[ny][nx],ny,nx])

    if len(fish_pos) == 0 :
        return [-1,-1,-1]

    fish_pos.sort(key = lambda x: (x[0],x[1],x[2]))
    return fish_pos[0]

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
shark_size = 2
cnt = 0 # 먹은 물고기.
cur_y,cur_x = 0,0
dy = [0,0,1,-1]
dx = [-1,1,0,0]
time = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9 :
            cur_y,cur_x = i,j
            grid[cur_y][cur_x] = 0

while True:
    t, cur_y,cur_x = bfs(cur_y,cur_x)
    if cur_y == -1 and cur_x == -1 : # 먹을 물고기 X
        break
    grid[cur_y][cur_x] = 0 # 물고기 잡아먹고 맵 업데이트
    cnt+=1
    time+=t
    if shark_size == cnt :
        cnt = 0
        shark_size+=1
print(time) # 누적 시간을 리턴.
