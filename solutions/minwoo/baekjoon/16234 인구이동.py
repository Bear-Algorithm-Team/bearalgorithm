from collections import deque
n,l,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
t = 0

def bfs(y,x): # return: 연합국가갯수, 총인구합, 해당위치좌표들
    q = deque()
    visit[y][x] = 1
    q.append([y,x])
    pos = [[y,x]]
    population = board[y][x]
    region = 1
    while q :
        y,x = q.popleft()
        for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
            ny = y+dy
            nx = x+dx
            if 0<=ny<n and 0<=nx<n and not visit[ny][nx] and l<=abs(board[ny][nx] - board[y][x])<=r:
                visit[ny][nx] = 1
                q.append([ny,nx])
                pos.append([ny,nx])
                population+=board[ny][nx]
                region+=1
    return region,population,pos

def move(move_info):
    for _move_info in move_info :
        region,population,pos = _move_info
        carry = population // region # 배치시킬 인원
        for y,x in pos :
            board[y][x] = carry

while True :
    visit = [[0]*n for _ in range(n)]
    move_info = []
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                region,population,pos = bfs(i,j)
                if region > 1 :
                    move_info.append([region,population,pos])
    if len(move_info) == 0 : # 국경이 모두 닫혀있을 때
        break
    move(move_info) # 인구이동 시작
    t+=1
print(t)