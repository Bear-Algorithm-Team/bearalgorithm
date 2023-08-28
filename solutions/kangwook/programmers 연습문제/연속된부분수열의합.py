def solution(sequence, k):
    s, now_sum = 0, 0
    answer = []
    for idx, num in enumerate(sequence):
        now_sum += num
        while now_sum > k:
            now_sum -= sequence[s]
            s += 1
        if now_sum == k:
            answer.append([s, idx])
    return sorted(answer, key=lambda x: x[1] - x[0])[0]
