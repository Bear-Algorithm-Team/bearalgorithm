
T = int(input())
for test_case in range(1, T + 1):
    '''

    x = x0 * 3^0 + x1 * 3^1 + ... + xn * 3^n
    y = y0 * 3^0 + y1 * 3^1 + ... + yn * 3^n
    
    이 문제 핵심은 x_t가 0이면 y_t는 0이 아니어야 하고 반대도 마찬가지라는 거.
    그냥 x, y를 3진법으로 변환해서 x_t, y_t 확인하면 되는 문제.

    '''
    
    x, y = map(int, input().split())
    
    def check_if_digits_not_zero(x):
        """
        
        매 루프마다 x를 3으로 나누고 그 나머지가 0 아니면 result에 (1 << t) 더한다.

        근데 만약 2라면?
        이건 현재 자리수가 -1이라는 의미.
        그리고 이보다 윗자리수에 +1이 있다는 의미.

        결과적으로 각 자릿수에 해당하는 x_t가 0인지 아닌지 여부가 1, 0으로 기록된 2진수가 리턴된다.
        
        """
        result, t = 0, 0
        while x:
            digit = x % 3
            result += int(digit != 0) << t
            x //= 3
            if digit == 2:
                x += 1
            t += 1
        return result
    
    sum_digits = check_if_digits_not_zero(x) + check_if_digits_not_zero(y)
    ans = "yes" if sum_digits & (sum_digits + 1) == 0 else "no" # 주어진 수가 2^n꼴인지 확인하는 비트연산식.
    print(f"#{test_case} {ans}")
