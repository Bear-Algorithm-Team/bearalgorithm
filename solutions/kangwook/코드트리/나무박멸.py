n, m, k, c = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
herbicide = [[0] * n for _ in range(n)]

def grow_trees(grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0: continue
            cells_with_trees = 0
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 0:
                    cells_with_trees += 1
            grid[i][j] += cells_with_trees
    return grid

def spread_trees(grid):
    grid_updated = [grid[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0: continue
            empty_cells = []
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and herbicide[nr][nc] == 0:
                    empty_cells.append([nr, nc])
            for nr, nc in empty_cells:
                grid_updated[nr][nc] += grid[i][j] // len(empty_cells)
    return grid_updated

def calc_trees_in_cell(i, j):
    cnt = grid[i][j]
    cells_group = [(i, j)]
    for dr, dc in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        for l in range(k):
            nr, nc = i + dr * (l + 1), j + dc * (l + 1)
            if not(0 <= nr < n and 0 <= nc < n) or grid[nr][nc] < 0:
                break
            cells_group.append((nr, nc))
            cnt += grid[nr][nc]
            if grid[nr][nc] == 0: 
                break
    return cnt, cells_group

def eliminate_trees(grid):
    trees_in_cells = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0: continue
            cnt, cells_group = calc_trees_in_cell(i, j)
            trees_in_cells.append((cnt, -i, -j, cells_group))
    trees_in_cells.sort(reverse=True)

    if len(trees_in_cells) == 0: 
        return 0

    answer, _, _, cells_group = trees_in_cells[0]
    for i in range(n):
        for j in range(n):
            if herbicide[i][j]:
                herbicide[i][j] -= 1
    for nr, nc in cells_group:
        herbicide[nr][nc] = c
        grid[nr][nc] = 0
    return answer

trees_eliminated = 0
for i in range(m):
    grid = grow_trees(grid)
    grid = spread_trees(grid)
    trees_eliminated += eliminate_trees(grid)

print(trees_eliminated)
