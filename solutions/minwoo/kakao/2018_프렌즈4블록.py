from collections import deque


def solution(m, n, board):  # m : 높이 n:가로
    board = [list(board[i]) for i in range(m)]
    remove_cnt = 0

    while True:
        remove_set = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '#' and board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and \
                        board[i][j] == board[i + 1][j + 1]:
                    remove_set.add((i, j))
                    remove_set.add((i, j + 1))
                    remove_set.add((i + 1, j))
                    remove_set.add((i + 1, j + 1))
        if len(remove_set) == 0:
            break

        for y, x in remove_set:  # 맵에서 지운다.
            board[y][x] = '#'
            remove_cnt += 1

        # 아래로 요소들 이동.
        for j in range(n):
            q = deque()  # 블록을 한칸씩 내리는 로직을 BFS로 진행.
            for i in range(m - 2, -1, -1):  #
                if board[i][j] != '#':  # 움직일 수 있는 블럭들을 삽입한다.
                    q.append((i, j))
            while q:
                y, x = q.popleft()
                if 0 <= y + 1 < m and board[y][x] != '#' and board[y + 1][x] == '#':
                    board[y + 1][x] = board[y][x]  # 이동을 먼저 시킴.
                    board[y][x] = '#'  # 이동전의 블럭을 없앰
                    q.append((y + 1, x))  # 이동한 좌표를 다시 큐에삽입.
    return remove_cnt
