from collections import deque

n,k = map(int,input().split())
convey = deque(map(int,input().split()))
robot = deque([0]*n)
t = 1
zero_cnt = 0
while True :
    #1 벨트, 로봇 회전.
    convey.appendleft(convey.pop())
    robot.pop()
    robot.appendleft(0)
    robot[-1] = 0
     #내구도 zero 인 컨베이어
    #2 먼저 올라간 순서대로 로봇 이동
    for i in range(len(robot)-1,0,-1):
        if convey[i] > 0 and robot[i-1] and not robot[i] :
            robot[i-1],robot[i] = 0,1
            convey[i]-=1 # 내구도 감소
            if convey[i] == 0 :
                zero_cnt +=1
    #3 첫번째 컨베이어에 로봇 올리기.
    if convey[0] > 0 :
        robot[0] = 1
        convey[0]-=1
        if convey[0] == 0 :
            zero_cnt +=1

    if zero_cnt >=k :
        break
    t += 1
print(t)

