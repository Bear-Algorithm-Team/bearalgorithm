def solution(name):
    qs, q = 0, [["A" * len(name), 0, 0]]
    if q[0][0] == name: return 0
    answer = -1
    while qs < len(q):
        now_str, now_pos, cnt = q[qs]
        # 1. 현재 위치의 알파벳을 변경한다.
        # 2. 다음 두 가지를 뻗는다.
        #    - 현재에서 오른쪽으로 변경할 알파벳을 찾아 거기로 이동한다.
        #    - 현재에서 왼쪽으로 변경할 알파벳을 찾아 거기로 이동한다.
        new_cnt = cnt
        if now_str[now_pos] != name[now_pos]:
            big, small = ord(now_str[now_pos]), ord(name[now_pos])
            if small > big: big, small = small, big
            new_cnt += min(big - small, small + 26 - big)
            now_str = now_str[:now_pos] + name[now_pos] + now_str[now_pos + 1:]
            if now_str == name:
                if answer == -1 or answer > new_cnt:
                    answer = new_cnt
                qs += 1
                continue
        
        for i in range(1, len(name)):
            new_pos = (now_pos + i) % len(name)
            if now_str[new_pos] != name[new_pos]:
                q.append([now_str, new_pos, new_cnt + i])
                break

        for i in range(1, len(name)):
            new_pos = (now_pos - i) % len(name)
            if now_str[new_pos] != name[new_pos]:
                q.append([now_str, new_pos, new_cnt + i])
                break
        
        qs += 1
    return answer
