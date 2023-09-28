from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    x_max, y_max = 51, 51
    
    def in_square(cur_x, cur_y, nx, ny):
        mid_x, mid_y = (cur_x + nx) / 2, (cur_y + ny) / 2
        return any(x1 < mid_x < x2 and y1 < mid_y < y2 for x1, y1, x2, y2 in rectangle)
    
    def on_border(cur_x, cur_y, nx, ny):
        mid_x, mid_y = (cur_x + nx) / 2, (cur_y + ny) / 2
        return any((x1 < mid_x < x2 and (y1 == mid_y or y2 == mid_y)) 
                   or (y1 < mid_y < y2 and (x1 == mid_x or x2 == mid_x)) for x1, y1, x2, y2 in rectangle)

    q = deque([(characterX, characterY, 0)])
    visited = set()
    while q:
        cur_x, cur_y, cnt = q.popleft()
        if (cur_x, cur_y) == (itemX, itemY): return cnt
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = cur_x + dx, cur_y + dy
            if not(0 <= nx < x_max and 0 <= ny <= y_max) or (nx, ny) in visited \
                or in_square(cur_x, cur_y, nx, ny) or not on_border(cur_x, cur_y, nx, ny): continue
            visited.add((nx, ny))
            q.append((nx, ny, cnt + 1))
