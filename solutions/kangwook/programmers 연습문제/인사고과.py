def solution(scores):
    wanho = scores[0]

    # scores는 s[0]를 기준으로 내림차순, s[1]를 기준으로 오름차순 정렬을 한다.
    # 이렇게 하면 예를 들어 ... (4, 3), (4, 7), (3, 6), (3, 9) ... 이와 같은 꼴로 정렬된다.
    # 이 문제에서 가장 중요한 것은 뒤에 있는 원소 중 s[0]뿐 아니라 s[1]까지 모두 앞에 있는 원소보다 작은 것을 filtering 하는 작업인데,
    # 이와 같이 정렬하면 s[0]값과는 상관 없이 s[1]의 값이 꾸준히 증가하는지 여부만 확인하고 아닌 건 filtering 하면 된다.
    # 여기서 (3, 6)은 이전 대비 감소했으므로 filtering 돼야 한다.
    scores.sort(key=lambda s: (-s[0], s[1]))

    max_peer_score = 0
    wanho_rank = 1
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        
        # 앞의 원소 중 s[1]의 최댓값보다 현재 s[1]이 더 큰 경우만 계산하고 아닌 경우는 filtering 한다.
        if max_peer_score <= s[1]:
            # wanho보다 앞에 있는 사람 수 세기
            if sum(wanho) < sum(s):
                wanho_rank += 1

            # 갱신
            max_peer_score = s[1]
    return wanho_rank
