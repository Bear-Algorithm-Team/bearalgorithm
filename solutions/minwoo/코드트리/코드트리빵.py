from collections import deque
n,m = map(int,input().split())
g_map = [list(map(int,input().split())) for _ in range(n)]
store = [list(map(int,input().split())) for _ in range(m)]
store = [[pos[0]-1,pos[1]-1] for pos in store]

visit = [[0]*n for _ in range(n)]
dp = [[0]*n for _ in range(n)]
person = [] # 사람의 위치

dy = [-1,0,0,1]
dx = [0,-1,1,0]
t = 0

def finish(): # 모든 편의점에 도착했는지 검사.
    if len(person) != m :
        return False
    for i in range(m):
        if person[i] != store[i] :
            return False
    return True

def bfs_shortest_path(s_y,s_x):
    global visit,dp
    q = deque()
    q.append([s_y,s_x])
    visit = [[0] * n for _ in range(n)] # visit 초기화
    dp = [[0] * n for _ in range(n)]
    visit[s_y][s_x] = 1

    while q :
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i] , x+dx[i]
            if 0<=ny<n and 0<=nx<n and g_map[ny][nx] != 2 and not visit[ny][nx] : # 2는 방문할수 없는 베이스캠프.
                visit[ny][nx] = 1
                dp[ny][nx] = dp[y][x] + 1
                q.append([ny,nx])

def simulate():
    # 1번
    for i in range(len(person)) :
        if person[i] == store[i]: # 이미 편의점 도착한사람은 pass
            continue
        y,x = person[i]
        bfs_shortest_path(store[i][0],store[i][1]) # 편의점 -> 현재 사람위치

        min_cost = 10**8
        min_y,min_x = -1,-1
        for j in range(4):
            ny,nx = y+dy[j],x+dx[j]
            if 0<=ny<n and 0<=nx<n and visit[ny][nx] and g_map[ny][nx] != 2 :
                if min_cost > min(min_cost,dp[ny][nx]):
                    min_y,min_x = ny,nx # 다음갈 방향 업데이트.
        person[i] = [min_y,min_x]  # 업데이트
        print(person)
    # 2번
    for i in range(len(person)):
        if store[i] == person[i] :
            g_map[person[i][0]][person[i][1]] = 2

    # 3번 
    if t<=m : # 편의점 -> 베이스캠프
        bfs_shortest_path(store[t-1][0],store[t-1][1])
        min_cost = 10**8
        min_y,min_x = -1,-1
        for i in range(n): # 최단거리 basecamp를 찾음.
            for j in range(n):
                if g_map[i][j] == 1 and visit[i][j] and min_cost > dp[i][j]:
                    min_cost = min(min_cost,dp[i][j])
                    min_y,min_x = i,j
        person.append([min_y,min_x]) # 최소거리 베이스캠프위치 삽입.
        g_map[min_y][min_x] = 2 # 해당 좌표는 이제 방문 불가.

while True :
    t+=1
    simulate()
    if finish(): # 모두 편의점에 도착했는지 판별
        break

print(t)

# 입력
# 5 3
# 0 0 0 0 0
# 1 0 0 0 1
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 1
# 2 3
# 4 4
# 5 1
