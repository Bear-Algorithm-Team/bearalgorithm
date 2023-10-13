def solve():
    def is_finish():
        for i in range(n):
            for j in range(n):
                if shark_board[i][j] > 1 :
                    return 0
        return 1

    def spray_smell():
        for i in range(n):
            for j in range(n):
                if shark_board[i][j] > 0 :
                    smell_board[i][j] = k
                    num_smell_board[i][j] = shark_board[i][j]
    def move():
        new_shark_board = [[0]*n for _ in range(n)]
        directions = [[],[-1,0],[1,0],[0,-1],[0,1]] # 북 남 서 동
        for i in range(n):
            for j in range(n):
                if shark_board[i][j] == 0 :
                    continue
                shark_num = shark_board[i][j] 
                cur_dir = shark_direction[shark_num]
                candidates = [] # 정렬조건: 1. 아무냄새없는칸. 2.자신이 있는칸 방향 우선순위는 딕셔너리에서 찾음

                for priority_idx in range(len(dir_priority[shark_num][cur_dir])):
                    d = dir_priority[shark_num][cur_dir][priority_idx] 
                    dy,dx = directions[d]
                    ny,nx = dy+i,dx+j
                    if 0<=ny<n and 0<=nx<n : # 아무냄새가 없는 칸을 다음방향으로 . 2번째 : 자신의 냄새가 있는 칸. 3번째. 우선순위
                        if smell_board[ny][nx] ==0 :
                            candidates.append([0,priority_idx,d]) 
                        else :
                            if num_smell_board[ny][nx] == shark_num:
                                candidates.append([1,priority_idx,d])
                candidates.sort(key = lambda x : (x[0],x[1]))
                _,_,next_dir = candidates[0]
                dy,dx = directions[next_dir]
                ny,nx = dy+i,dx+j
                shark_direction[shark_num] = next_dir

                if new_shark_board[ny][nx] == 0 or shark_num < new_shark_board[ny][nx]: # 번호가 작은 상어만 들어갈 수 있음.
                    new_shark_board[ny][nx] = shark_board[i][j]
        return new_shark_board

    def clear_smell():
        for i in range(n):
            for j in range(n):
                if smell_board[i][j] > 0 :
                    smell_board[i][j] -=1
                    if smell_board[i][j] == 0 :
                        num_smell_board[i][j] = 0 # 해당위치의 상어냄새 삭제

    n, m, k = map(int, input().split()) #nxn, 상어갯수, k: 체취지속시간
    shark_board = [list(map(int, input().split())) for _ in range(n)]
    smell_board = [[0]*n for _ in range(n)]
    num_smell_board = [[0]*n for _ in range(n)]
    shark_direction = [0]+list(map(int,input().split()))
    dir_priority = dict() # 문제에 주어진 패턴으로 중첩 딕셔너리로 선언
    for shark_num in range(m):
        dir_priority[shark_num + 1] = {}
        for i in range(4):
            directions = list(map(int,input().split()))
            dir_priority[shark_num+1].update({i+1:directions})
    
    time = 0
    while True :
        time +=1
        spray_smell()
        shark_board = move()
        clear_smell()
        if time > 1000 or is_finish():
            break
    return -1 if time > 1000 else time
print(solve())

