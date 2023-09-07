def check_validity(s):
    if len(s) == 1: return 1
    now_pos = len(s) // 2
    if s[now_pos] == "1":
        return check_validity(s[:now_pos]) & check_validity(s[now_pos + 1:])
    else:
        return 1 if s.count("0") == len(s) else 0

def solution(numbers):
    answer = []
    for num in numbers:
        s = bin(num).replace('0b', '')
        n = 0
        while (1 << n) - 1 < len(s):
            n += 1
        s = s.rjust((1 << n) - 1, '0')
        answer.append(check_validity(s))
    return answer
