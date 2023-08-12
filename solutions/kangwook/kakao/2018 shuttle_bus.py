from typing import List

ONE_DAY_MIN = 1440
ONE_HOUR_MIN = 60
FIRST_BUS_MIN = 540

"""

1. 문제 설명
https://school.programmers.co.kr/learn/courses/30/lessons/17678#
- 버스에 타려는 승객들이 하루 동안에 몇분 몇분에 역에 도착하는지가 주어지고, 
  9시부터 오는 셔틀이 총 몇대가 몇분 간격으로 오는지, 한 대당 정원이 얼마인지 주어질 때, 
  콘이 버스에 타긴 타도록 하되 그 중 가장 늦은 시간이 언제인지를 구하는 문제.

2. 풀이
- 하루가 1440분밖에 안되기 때문에, 0시 0분을 기준으로 0분부터 1440분까지 경과하면서 각 분마다 어떤 일이 일어나는지를 시뮬레이션하면 간단히 풀 수 있다.
- 따라서 시간복잡도가 O(1)이나, 메인 코드가 돌아가기 전에 전처리가 필요하며 이것이 O(n) 걸릴 수 있다.

3. 주의할 점
- 크루의 대기열이 증가하는 속도와 버스가 도착하는 속도가 서로 다를 수 있다. 예를 들어 0시 10분에 크루가 
  20-30명 들어올 수 있는데 버스는 5명 정원짜리가 2시간 간격으로 5대 오는 상황이 있을 수 있다. 이처럼 
  시뮬레이션 문제는 얼핏 보면 떠올리기 어려운 극단적인 상황이 나타날 수 있으며, 이는 같은 상황에서 숫자만 
  조금 달라져도 나타나는 상황일 수 있다. 평소 문제를 많이 푸는 연습이 돼있다면 이런 상황을 빠르게 떠올려 깔끔하게 대처할 수 있다.

"""

def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    bus_arrival_minute: List[bool] = [False] * ONE_DAY_MIN
    crew_num_minute: List[int] = [0] * (ONE_DAY_MIN + 1)

    for i_minute in range(n):
        bus_arrival_minute[FIRST_BUS_MIN + i_minute * t] = True

    for time in timetable:
        hour: int = int(time[:2]) * ONE_HOUR_MIN
        minute: int = int(time[3:])
        crew_num_minute[hour + minute] += 1

    answer_minute: int = 0
    crew_num_queue: int = 0
    buses_to_come: int = n
    for i_minute in range(FIRST_BUS_MIN + (n - 1) * t + 1):
        # i_minute에 크루들이 줄 서있는 경우에,
        # 콘을 'i_minute - 1'분에 줄세우면 마지막 버스에라도 탈 수 있다면
        # 일단 콘을 이때 버스 태우는 게 답이라고 전제하고 answer를 업데이트.
        # 이 이후 시점에도 버스에 탈 수 있다면 answer는 그때 덮어씌워질 것.
        # 아니라면 여기서 업데이트된 값이 리턴값이 될 것.
        if crew_num_minute[i_minute] > 0 and crew_num_queue + 1 <= m * buses_to_come:
            answer_minute = i_minute - 1

        crew_num_queue += crew_num_minute[i_minute]

        if not bus_arrival_minute[i_minute]:
            continue

        buses_to_come -= 1
        if crew_num_queue >= m:
            crew_num_queue -= m
        else:
            # 대기열 모든 크루가 버스 정원보다 적고 1명 이상 더 탈 수 있는 경우,
            # 이때는 콘이 i_minute에 줄을 서더라도 무조건 버스를 탈 수 있음.
            crew_num_queue = 0
            answer_minute = i_minute

    hh: str = str(answer_minute // 60).zfill(2)
    mm: str = str(answer_minute % 60).zfill(2)
    return f"{hh}:{mm}"
