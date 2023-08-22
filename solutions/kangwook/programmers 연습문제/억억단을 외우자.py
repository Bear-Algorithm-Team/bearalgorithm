def solution(e, starts):
    div_num = [0] * (e + 1)
    for i in range(1, int(e ** 0.5) + 1):
        div_num[i * i] += 1
        for j in range(i * i + i, e + 1, i):
            div_num[j] += 2
            
    max_div_pair = [0, 0]
    max_div = [0] * (e + 1)
    for i in range(e, 0, -1):
        if div_num[i] >= max_div_pair[1]:
            max_div_pair = [i, div_num[i]]
        max_div[i] = max_div_pair[0]
    return [max_div[s] for s in starts]
