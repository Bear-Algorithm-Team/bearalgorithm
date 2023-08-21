from collections import deque

def solution(routes):
    camera_pos = -30001
    routes.sort(key = lambda x : x[1])
    routes = deque(routes)
    cnt = 0
    while routes : 
        s,e = routes.popleft()
        if camera_pos < s: # 카메라 설치 
            camera_pos = e 
            cnt+=1

    return cnt