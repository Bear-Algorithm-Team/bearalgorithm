from collections import deque

n,m = map(int,input().split())
grid = [input() for _ in range(n)]
visit = [[[0]*m for _ in range(n)] for _ in range(2)]
cache = [[[0]*m for _ in range(n)] for _ in range(2)]
dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(i,j):
    q = deque()
    visit[0][i][j] = 1
    cache[0][i][j] = 1
    q.append([0,i,j])

    while q :
        z,y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if z == 0 :  # 벽을 부술 수 있다
                if 0<=ny<n and 0<=nx<m and visit[0][ny][nx] == 0 and grid[ny][nx] == "0":  
                    visit[0][ny][nx] = 1
                    cache[0][ny][nx] = cache[0][y][x]+1
                    q.append([0,ny,nx])
                elif 0<=ny<n and 0<=nx<m and visit[1][ny][nx] == 0 and grid[ny][nx] == "1":
                    visit[1][ny][nx] = 1
                    cache[1][ny][nx] = cache[0][y][x] + 1
                    q.append([1,ny,nx])

            elif z == 1 : #벽을 부술 수 없고, 같은층으로만 이동한다.
                if 0<=ny<n and 0<=nx<m and visit[1][ny][nx] == 0 and grid[ny][nx] == "0" :
                    visit[1][ny][nx] = 1
                    cache[1][ny][nx] = cache[1][y][x] + 1
                    q.append([1,ny,nx])

bfs(0,0)

if cache[0][n-1][m-1] == 0 and cache[1][n-1][m-1] == 0 :
    print(-1)

elif cache[0][n-1][m-1] == 0 or cache[1][n-1][m-1] == 0: # 목적지에 도달할 수 없는 층이 있으므로
    print(max(cache[0][n-1][m-1], cache[1][n-1][m-1]))
else:
    print(min(cache[0][n - 1][m - 1], cache[1][n - 1][m - 1])) # 0층, 1층 중 도달할 수 있는 최솟값