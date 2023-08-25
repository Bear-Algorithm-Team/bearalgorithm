import heapq

def solution(jobs): # 일찍시작하는순, 길이가 짧은순으로 큐에 넣는다. 늦게 시작했더라도, 길이가 짧은애를 먼저 실행시켜야한다.
        q1 = [] # 일찍 들어온 순
        q2 = [] # 실행시간 짧은 순
        for job in jobs :
            heapq.heappush(q1,job)
        cur_e = 0
        ans= 0
        while len(q1) != 0 or len(q2) !=0:
            while q1 :  # 현재시각에 실행할 수 있는 프로그램을 대기큐에 올린다
                start,duration = q1[0]
                if cur_e >=start or len(q2) == 0:
                    start,duration = heapq.heappop(q1)
                    heapq.heappush(q2,[duration,start]) 
                else:
                    break
                    
            duration,start = heapq.heappop(q2)
            if cur_e < start : # 대기시간이 없는경우
                ans += duration 
                cur_e = start+duration
            else:
                ans += (cur_e-start + duration)
                cur_e = cur_e+duration
        return ans//len(jobs)