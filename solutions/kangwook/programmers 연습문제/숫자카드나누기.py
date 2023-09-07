import math

def divisible_a_no_b(arrayA, arrayB):
    """

    arrayA는 모두 나눠 떨어지게 하지만,
    arrayB의 어떤 원소도 나누지 못하는 가장 큰 정수를 찾아 리턴한다.
    그런 게 없다면 0을 리턴한다.

    그냥 arrayA의 최대공약수를 구한 다음에 그게 arrayB의 어떤 원소도 나누지 못하면 그걸 리턴하면 됨.
    더 작은 약수는 고려할 필요 없음.

    """

    gcd = arrayA[0]
    for num in arrayA:
        gcd = math.gcd(gcd, num)

    return gcd if all(x % gcd != 0 for x in arrayB) else 0

def solution(arrayA, arrayB):
    tmp1 = divisible_a_no_b(arrayA, arrayB)
    tmp2 = divisible_a_no_b(arrayB, arrayA)
    return max(tmp1, tmp2)
