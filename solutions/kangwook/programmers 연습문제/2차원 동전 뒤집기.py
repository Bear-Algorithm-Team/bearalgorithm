def solution(beginning, target):
    m, n = len(beginning), len(beginning[0])
    table = [[beginning[i][j] ^ target[i][j] for j in range(n)] for i in range(m)]

    rows_to_toggle = 0
    # table의 두 번째 행부터 조사해서, toggle해야만 첫 번째 행과 같은 모양이 나오는 행 개수를 센다.
    # 그렇게 나머지 행의 모양을 첫행과 똑같게 일치시키면, 그 다음에는 필요한 열만 toggle하면 된다.  
    for i in range(1, m):
        if table[i] != table[0]:
            rows_to_toggle += 1
            
            # toggle하더라도 첫 번째 행과 모양이 다르다면 애초에 target을 못 만드는 입력.
            if list(map(lambda x: x ^ 1, table[i])) != table[0]:
                return -1

    return min(rows_to_toggle + sum(table[0]), (m - rows_to_toggle) + (n - sum(table[0])))
