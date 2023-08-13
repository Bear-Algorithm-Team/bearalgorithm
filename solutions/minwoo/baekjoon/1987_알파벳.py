# 재귀로 전방향을 탐색하면서, 백트래킹 사용
import sys
sys.setrecursionlimit(10**5)
def dfs(y,x,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        ny,nx = y+dy[i], x+dx[i]
        if 0<=ny<n and 0<=nx<m and not visit[ord(grid[ny][nx])-65] :
            visit[ord(grid[ny][nx])-65] = True
            dfs(ny,nx,cnt+1)
            visit[ord(grid[ny][nx]) - 65] = False


n,m = map(int,input().split())
grid = [input() for _ in range(n)]
visit = [0]*26
dy= [0,0,1,-1]
dx = [1,-1,0,0]
ans = 0
visit[ord(grid[0][0])-65] = True
dfs(0,0,1)
print(ans)

