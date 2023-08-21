n = 0

def assign_camp(base_map, dest):
    qs, q = 0, [[dest[0] - 1, dest[1] - 1]]
    is_visit = [[False for _ in range(n)] for _ in range(n)]
    is_visit[dest[0] - 1][dest[1] - 1] = True

    while qs < len(q):
        now_r, now_c = q[qs]

        if base_map[now_r][now_c] == 1:
            return now_r, now_c

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nr, nc = now_r + dr, now_c + dc
            if 0 <= nr < n and 0 <= nc < n and not is_visit[nr][nc] and base_map[nr][nc] != 2:
                is_visit[nr][nc] = True
                q.append([nr, nc])
        qs += 1

def main():
    global n

    n, m = map(int, input().split())

    base_map = [list(map(int, input().split())) for _ in range(n)]
    # 0: 이동 가능
    # 1: 베이스캠프
    # 2: 이동불가

    dest = [list(map(int, input().split())) for _ in range(m)]
    q = [[] for _ in range(m)]
    qs = [0 for _ in range(m)]
    is_visit = [[[False for _ in range(n)] for _ in range(n)] for _ in range(m)]

    time_min = 0
    num_of_arrival = 0
    while num_of_arrival < m:
        # 1. 현재(time_min분)보다 전에 베캠에 도착했던 사람들을 한칸씩 이동시킨다.
        #   - 이때, 이 중 누군가가 편의점에 도착했다면, 그 위치를 이동불가 처리 한다.
        # 2. 현재 베캠에 위치시킬 사람을 그 사람이 희망하는 편의점과 가까운 베캠에 위치시킨다.
        # 3. 모두 편의점에 도착할 때까지 반복한다.

        # 매 루프마다, 각 사람마다 BFS를 depth를 하나씩 늘려나가는 식으로 수행한다.
        for i in range(m):
            while qs[i] < len(q[i]) and q[i][qs[i]][2] == time_min - 1:
                now_r, now_c, depth = q[i][qs[i]]

                for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    nr, nc = now_r + dr, now_c + dc
                    if 0 <= nr < n and 0 <= nc < n and not is_visit[i][nr][nc] and base_map[nr][nc] != 2:
                        if nr == dest[i][0] - 1 and nc == dest[i][1] - 1:
                            num_of_arrival += 1
                            base_map[nr][nc] = 2
                            qs[i] = len(q[i])
                            break
                        else:
                            is_visit[i][nr][nc] = True
                            q[i].append([nr, nc, depth + 1])
                qs[i] += 1

        if time_min < m:
            camp_r, camp_c = assign_camp(base_map, dest[time_min])
            q[time_min].append([camp_r, camp_c, time_min])
            is_visit[time_min][camp_r][camp_c] = True
            base_map[camp_r][camp_c] = 2

        time_min += 1

    print(time_min)

main()
