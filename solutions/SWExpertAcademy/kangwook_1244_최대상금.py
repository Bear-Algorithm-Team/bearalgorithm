"""

1. 문제 설명
- n자리 자연수가 주어질 때, 각 자릿수를 m회 맞바꿔 만들 수 있는 가장 큰 수를 출력하는 문제.

2. 풀이
- 기본적으로 BFS를 돌며 모든 경우의 수를 고려하되, 문제의 조건을 고려하여 가지치기를 한다.
  - m회 교환하여 가까스로 크기순 정렬이 되거나, 정렬이 완성되지 않는 경우 -> brute force로 풀고 결과 출력
  - m회 미만 교환했음에도 이미 크기순 정렬이 되는 경우
    - 남은 횟수가 짝수: 거기서 바로 결과 출력
    - 남은 횟수가 홀수
       - 남은 횟수가 짝수면서 크기순 정렬이 되는 상황이 나올 때까지 brute force를 계속 한다.
       - 아무리 해도 안됐다면 끝 두 자리만 바꿔서 출력.
- 모든 경우의 수는 30C2 ^ 10 = 약 1천억이지만, 위와 같이 가지를 치면 훨씬 경우의 수가 줄어든다.

3. 고려할 점
- 처음에 'm회 미만 교환했음에도 이미 크기순 정렬이 됐는데 남은 횟수가 홀수면 바로 끝 두 자리만 바꿔서 출력한다'라고 단순하게 생각했으나 
  테스트 케이스 14/15개만 정답이 돼서 어디 버그가 있는 줄 알고 오래 시간낭비 함. 
- 가지치기를 잘 해야 하는 brute force 문제는 어느 정도 과감하게 가지를 칠 필요가 있기 때문에 그 로직이 맞다고 생각할 수 있는데, 
  그래도 정답이 나오지 않는다면 조금 더 깊게 생각할 필요가 있는듯. 과감하게 가지를 칠 때도 가지 치는 부분마다 조금 더 꼼꼼히 생각할 필요.

"""

def list_to_str(plate):
    return "".join(map(str, plate))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    plate, c_num = map(int, input().split())
    plate = list(map(int, str(plate)))
    sorted_plate = sorted(plate, reverse=True)

    q = [[0, plate]]
    is_visit = [set() for i in range(11)]
    is_visit[0].add(list_to_str(plate))
    answer_num, answer = 0, ""
    qs = 0
    while qs < len(q):
        if q[qs][1] == sorted_plate:
            answer_num, answer = q[qs][0], list_to_str(sorted_plate)
            if (c_num - answer_num) % 2 == 0: # 남은 횟수가 짝수회면 바로 종료.
                break
        if q[qs][0] == c_num: # 주어진 교환 횟수를 모두 마친 상황
            qs_plate_str = list_to_str(q[qs][1])
            if  qs_plate_str > answer:
                answer_num, answer = c_num, qs_plate_str
            qs += 1
            continue # 여기서는 더 이상 뻗어나가지 않는다.

        for i in range(len(plate)):
            for j in range(i +1, len(plate)):
                q.append([q[qs][0] + 1, q[qs][1][:]])
                q[-1][1][i], q[-1][1][j] = q[-1][1][j], q[-1][1][i]
                new_plate_str = list_to_str(q[-1][1])
                if new_plate_str not in is_visit[q[-1][0]]:
                    is_visit[q[-1][0]].add(new_plate_str)
                else:
                    q.pop()

        qs += 1
    if (c_num - answer_num) % 2 == 1 and len(answer) >= 2:
        answer_list = list(map(int, answer))
        answer_list[-2], answer_list[-1] = answer_list[-1], answer_list[-2]
        answer = list_to_str(answer_list)
    print(f"#{test_case} {answer}")
