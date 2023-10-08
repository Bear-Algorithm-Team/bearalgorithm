n,m,k,c = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
kill = [[0]*n for _ in range(n)]
ans = 0

def step1(): # 나무성장
    for i in range(n):
        for j in range(n):
            adj_tree = 0
            if board[i][j] > 0 :
                for dy,dx in ((0,-1),(0,1),(1,0),(-1,0)):
                    ny = i+dy
                    nx = j+dx
                    if 0<=ny<n and 0<=nx<n and board[ny][nx] > 0 :
                        adj_tree +=1
                board[i][j] += adj_tree

def step2(): # 번식
    new_board = [[0]*n for _ in range(n)] # 번식 판
    for i in range(n):
        for j in range(n):
            adj_tree = 0
            if board[i][j] > 0:
                for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
                    ny = i + dy
                    nx = j + dx
                    if 0<=ny<n and 0<=nx<n and board[ny][nx] == 0 and kill[ny][nx] == 0: # 번식이 가능한칸을 카운트
                        adj_tree +=1

                if adj_tree == 0 : # zero devide 방어코드
                    continue
                for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)): # 번식을 새로운 판에 진행.
                    ny = i+dy
                    nx = j+dx
                    if 0<=ny<n and 0<=nx<n and board[ny][nx] == 0 and kill[ny][nx] == 0:
                        new_board[ny][nx] += (board[i][j] // adj_tree)

    for i in range(n): # 번식판 병합
        for j in range(n):
            board[i][j] += new_board[i][j]

def step3():
    cnt = 0
    t_y,t_x = -1,-1
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 :
                trees = calc_kill(i,j) # 제초제를 뿌려본다.
                if trees > cnt :
                    cnt = trees
                    t_y,t_x = i,j
    if cnt > 0: #나무가 없는곳은 뿌릴필요없음.
        spray(t_y,t_x)


def calc_kill(y,x):
    cnt = board[y][x] # 박멸한 나무의 갯수.
    for z in range(1,k+1) : # z-1 거리에 있는애가 0 이면 진행하지않는다.
        for dy,dx in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ny = y + z*dy
            nx = x + z*dx
            if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1:
                for prev_z in range(z): # 해당 대각선 방향으로 진행하되, 0 이있으면, 제초제는 확장하지 못한다.
                    if board[y + prev_z * dy][x + prev_z * dx] <= 0:
                        break
                else:
                    cnt += board[ny][nx]
    return cnt

def spray(y,x):
    global ans
    targets = [[y,x]]
    for z in range(1,k+1) :
        for dy,dx in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ny = y+z*dy
            nx = x+z*dx
            # 0까지는 제초제가 뿌려진다.
            if 0<=ny<n and 0<=nx<n and board[ny][nx] != -1:
                for prev_z in range(z): # 해당 대각선 방향으로 진행하되, 0 이있으면, 제초제는 확장하지 못한다.
                    if board[y + prev_z * dy][x + prev_z * dx] <= 0:
                        break
                else:
                    targets.append([ny, nx])

    for ty,tx in targets :
        ans += board[ty][tx]
        board[ty][tx] = 0
        kill[ty][tx] = time+c # 약을 뿌린다.

def clear_kill():
    for i in range(n):
        for j in range(n):
            if kill[i][j] + 1 == time :
                kill[i][j] = 0

time = 0
while True :
    if time == m :
        break
    clear_kill()
    step1()
    step2()
    step3()
    time+=1
print(ans)