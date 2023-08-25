# s: 속력 d: 이동방향 z: 크기
def move_and_rotate(shark):
    global new_grid
    y, x, s, d, z = shark
    cur_y,cur_x,cur_s,cur_d,cur_z = y, x, s, d, z

    while cur_s:
        ny, nx = cur_y + dy[cur_d], cur_x + dx[cur_d]
        if not (0 <= ny < n and 0 <= nx < m):
            cur_d = (cur_d + 2) % 4
        ny, nx = cur_y + dy[cur_d], cur_x + dx[cur_d]
        cur_y, cur_x = ny, nx
        cur_s -= 1

    if len(new_grid[cur_y][cur_x]) > 0: # 상어가 존재하는 경우.
        _, _, _, _, exist_z = new_grid[cur_y][cur_x]
        if exist_z > z:  # 기존에 존재하는 상어가크면
            return
    new_grid[cur_y][cur_x] = [cur_y, cur_x, s, cur_d, z]  # 상어는 동시에 움직이기 때문에, 맵을 한번에 업데이트해줘야한다


def eat_shark(shark):
    global ans
    y, x, s, d, z = shark
    grid[y][x] = []  # 낚시왕이 상어를 건짐
    ans += z


def move_shark(): # 전체 격자판을 순회하며 상어를 이동.
    global grid,new_grid
    new_grid = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cur_shark = grid[i][j]
            if len(cur_shark) > 0:  # 해당 좌표에 상어가 있을때, 상어를 이동한다
                move_and_rotate(cur_shark)
    grid = new_grid # 모든상어를 움직인후, 새로운 맵으로 업데이트한다.

n,m,k = map(int,input().split())
grid = [[[] for _ in range(m)] for _ in range(n)]
new_grid = [[[] for _ in range(m)] for _ in range(n)]
dy = [-1,0,1,0] # up right bottom left
dx = [0,1,0,-1]
ans = 0

for i in range(k):
    r,c,s,d,z = map(int,input().split())
    if d == 1 : # 180도 회전 mod 연산을 쉽게 하기위해서 커스텀한다.
        d = 0
    elif d == 2 :
        d = 2
    elif d == 3:
        d =  1
    elif d == 4:
        d = 3
    grid[r-1][c-1] = [r-1,c-1,s,d,z]

for j in range(m) : # 현재 어부의 열
    for i in range(n) : # 상어 행 순회
        shark = grid[i][j]
        if len(shark) > 0 : # 땅과 가까운 상어를 건진다.
            eat_shark(shark)
            break
    move_shark()

print(ans)

