from collections import deque
q = deque()
n = int(input())
q.append((1,0,[1]))
visit = [0]*(n+1)
while q :
    cur,cost, candidate = q.popleft()
    visit[cur] = 1
    if cur == n :
        print(cost)
        print(*candidate[::-1])
        exit(0)
    if cur*3 <= n and not visit[cur*3]:
        q.append((cur*3,cost+1,candidate+[cur*3]))
        visit[cur*3] = 1
    if cur*2 <= n and not visit[cur*2]:
        q.append((cur*2,cost+1,candidate+[cur*2]))
        visit[cur*2] = 1
    if cur+1 <= n and not visit[cur+1] :
        q.append((cur+1,cost+1,candidate+[cur+1]))
        visit[cur+1] = 1