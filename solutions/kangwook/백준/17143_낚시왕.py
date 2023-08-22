R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
for i in range(M):
    sharks[i][0] -= 1
    sharks[i][1] -= 1
D = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]

def assign_sharks():
    fishing_map = [[-1 for _ in range(C)] for _ in range(R)]
    for idx, shark in enumerate(sharks):
        r, c, s, d, z = shark
        fishing_map[r][c] = idx
    return fishing_map

def update_fishing_map():
    fishing_map = [[-1 for _ in range(C)] for _ in range(R)]
    for idx, shark in enumerate(sharks):
        if not shark: continue 
        r, c, s, d, z = shark

        # 1초 뒤 상어의 위치 계산하기.
        # 예를 들어 R = 4라면, 다음 방식으로 1초 뒤 상어 위치를 찾을 수 있다. 
        # 0 1 2 3 4 5 6
        # 0 1 2 3 2 1 0
        # 원래 2 위치에 있던 상어가 초당 2칸 이동한다면, 2초 뒤에는 2 위치에 도착.
        # 즉, (2 * R - 2) 주기로 위 패턴이 반복된다.
        nr, nc = r + D[d][0] * s, c + D[d][1] * s

        nr %= 2 * R - 2
        nc %= 2 * C - 2

        # 일단 (2 * R - 2)로 나눈 나머지를 구하되, nr, nc가 R, C보다 크면 뒤집어진 위치를 계산하고, 상어 이동 방향을 뒤집는다.
        if nr >= R: 
            nr  = 2 * R - nr - 2
            sharks[idx][3] = d + (1 if d % 2 else -1)
        if nc >= C: 
            nc  = 2 * C - nc - 2
            sharks[idx][3] = d + (1 if d % 2 else -1)

        # 상어의 현재 위치를 업데이트하고, 새 2차원 배열에 상어를 배치시켜 이를 리턴한다.
        sharks[idx][0], sharks[idx][1] = nr, nc
        if fishing_map[nr][nc] == -1:
            fishing_map[nr][nc] = idx
        elif sharks[fishing_map[nr][nc]][4] < z:
            sharks[fishing_map[nr][nc]] = []
            fishing_map[nr][nc] = idx
        elif sharks[fishing_map[nr][nc]][4] > z:
            sharks[idx] = []
    return fishing_map

def main():
    global sharks

    # 2차원 배열에 상어를 배치시킨다. 낚시할 상어 찾기에 필요.
    fishing_map = assign_sharks()
    
    answer = 0
    for i in range(C):
        for j in range(R):
            # 가장 윗행의 상어를 낚시한다.
            if fishing_map[j][i] != -1:
                answer += sharks[fishing_map[j][i]][4]
                sharks[fishing_map[j][i]] = []
                break

        # 시간이 1초 지난 뒤 map을 업데이트한다.
        fishing_map = update_fishing_map()

    print(answer)
        
main()
