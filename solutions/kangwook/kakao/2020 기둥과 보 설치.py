def solution(n, build_frame):
    answer = []
    pillars = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    beams = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    def stable(x, y, a):
        if pillars[x][y - 1]:
            return True

        if a == 0:
            return y == 0 or beams[x][y] or beams[x - 1][y]

        return pillars[x + 1][y - 1] or (beams[x - 1][y] and beams[x + 1][y])

    def all_stable(answer):
        for x, y, a in answer:
            if not stable(x, y, a):
                return False
        return True

    def update_map(x, y, a, val):
        if a == 0:
            pillars[x][y] = val
        elif a == 1:
            beams[x][y] = val

    for x, y, a, b in build_frame:
        if b == 1 and stable(x, y, a):
            update_map(x, y, a, True)
            answer.append([x, y, a])
        elif b == 0:
            update_map(x, y, a, False) # 일단 제거
            if all_stable(answer):
                answer.remove([x, y, a])
            else:
                update_map(x, y, a, True) # 원상복구
    return sorted(answer)
