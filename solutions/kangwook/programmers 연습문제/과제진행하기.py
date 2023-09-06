def solution(plans):
    plans = sorted(map(lambda x: [
                                   x[0],
                                   int(x[1][:2]) * 60 + int(x[1][3:]),
                                   int(x[2]),
                                 ], plans), key=lambda x: x[1])
    result = []
    st = []
    cur_time = 0
    for plan in plans:
        # cur_time을 next_time으로 갱신할 것.
        next_time = plan[1]
        
        # 현재 과목을 스택에 넣고 cur_time 갱신할 건데, 그 전에 스택의 기존 최상위 과제들을 마쳐도 될 시간 여유가 있으면 이들을 모두 pop한다.
        while len(st) != 0 and cur_time + st[-1][2] <= next_time:
            subject, _, duration = st.pop()
            cur_time += duration
            result.append(subject)

        if len(st) != 0:
            # 스택의 기존 최상위 과제는 next_time - cur_time만큼 수행함
            st[-1][2] -= next_time - cur_time

        # 스택에 현재 과제를 추가하고 cur_time을 갱신한다.
        st.append(plan)
        cur_time = next_time

    # 스택에 남아있는 과제들을 result에 추가해서 리턴한다.
    return result + list(list(zip(*st))[0][::-1])
