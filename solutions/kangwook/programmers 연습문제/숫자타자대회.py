import sys
sys.setrecursionlimit(10**9)

num_pos = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
dy = []
# dy[i][좌우 엄지 위치] = 현재 손가락 상태에서 i번째 수를 누른 후 거기서 가지를 뻗어 
#                      결국 모든 숫자를 누르게 되었을 때, 여기서부터 추가로 비용 들여야 하는
#                      가중치 합 최솟값.

def calc_weight(start, target):
    if start == target:
        return 1

    s_r, s_c = num_pos[int(start)]
    t_r, t_c = num_pos[int(target)]

    longer_len = max(abs(s_r - t_r), abs(s_c - t_c))
    shorter_len = min(abs(s_r - t_r), abs(s_c - t_c))
    return shorter_len * 3 + (longer_len - shorter_len) * 2

def dfs(numbers, left, right, idx):
    
    if idx == len(numbers):
        return 0
    if len(dy) == idx:
        dy.append({})
    if left + right in dy[idx]:
        return dy[idx][left + right]
    
    dy[idx][left + right] = 10**9
    if left != numbers[idx]:
        dy[idx][left + right] = min(dy[idx][left + right], calc_weight(right, numbers[idx]) + dfs(numbers, left, numbers[idx], idx + 1))
    
    if right != numbers[idx]:
        dy[idx][left + right] = min(dy[idx][left + right], calc_weight(left, numbers[idx]) + dfs(numbers, numbers[idx], right, idx + 1))
    
    return dy[idx][left + right]

def solution(numbers):
    return dfs(numbers, "4", "6", 0)