import copy

def move_shark_get_movable_pos(board,shark):
    # shark 의 진행방향으로 쭉 탐색해본다.
    shark_y, shark_x, shark_dir, _ = shark
    dy,dx = dir[shark_dir]
    movable = []
    for i in range(4):
        ny,nx = shark_y+i*dy, shark_x+i*dx
        if 0<=ny<4 and 0<=nx<4 and board[ny][nx] > 0 :
           movable.append([ny,nx])
    return movable

def move_fish(board,fish_dir,shark):
    for fish_num in range(1,17):
        skip = False
        for i in range(4):
            for j in range(4):
                if board[i][j] != fish_num :
                    continue
                cur_dir = fish_dir[fish_num]
                for _ in range(8): # 8개의 방향대로 수행해봄.
                    dy,dx = dir[cur_dir]
                    ny, nx = dy + i, dx + j
                    if 0<=ny<4 and 0<=nx<4 and board[ny][nx] >= 0 and [ny,nx] != [shark[0],shark[1]]:
                        fish_dir[fish_num] = cur_dir # 현재 물고기방향 업데이트.
                        board[ny][nx],board[i][j] = board[i][j], board[ny][nx] # 좌표 swap
                        skip = True
                        break # 물고기 이동한경우.
                    cur_dir = (cur_dir + 1) % 8
                if skip: # 물고기를 옮겼으면 , 2중for문을 바로 탈출해야한다
                    break
            if skip:
                break

def solve(board,fish_dir,shark): 
    global ans
    board = copy.deepcopy(board)
    fish_dir = copy.copy(fish_dir)
    shark_y,shark_x,shark_dir,shark_eat = shark 
    shark_eat += board[shark_y][shark_x] # 상어가 잡아먹은 물고기 번호 합
    shark_dir = fish_dir[board[shark_y][shark_x]] # 잡아먹은 물고기 방향을 물려받음.
    board[shark_y][shark_x] = 0 # 물고기를 잡아먹는다.

    move_fish(board,fish_dir,[shark_y,shark_x,shark_dir,shark_eat]) # 물고기 이동
    movable_pos = move_shark_get_movable_pos(board,[shark_y,shark_x,shark_dir,shark_eat]) # 상어를 움직일수 있는 좌표를 탐색해본다.
    if len(movable_pos) == 0 : # 재귀 종료 조건 (상어가 움직일수 있는 좌표가 없을 때.)
        ans = max(ans, shark_eat)
    for m_y,m_x in movable_pos :
        solve(board,fish_dir,[m_y,m_x,shark_dir,shark_eat])

board = []
fish_dir = [0]*17 # 물고기 현재 방향 
shark = [0,0,0,0] # y,x,dir,먹은 물고기번호 합
dir = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
ans = 0 
for _ in range(4):
    temp = []
    arr = list(map(int,input().split()))
    for i in range(0,len(arr),2):
        temp.append(arr[i]) # board에는 물고기번호만 저장한다.
        fish_dir[arr[i]] = arr[i+1]-1 # fish_dir에는 해당 물고이의 방향을 저장 
    board.append(temp)
solve(board,fish_dir,shark)
print(ans)

