from collections import deque

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    dp = [10**8]*(n+1)
    q = deque()
    
    summits = set(summits)
    for i in range(len(paths)):
        a,b,c = paths[i]
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    for i in range(len(gates)):
        q.append(gates[i]) # 시작지점을 모두 초기화한다.
        dp[gates[i]] = 0 # 시작점 dp 초기화

    while q :
        cur = q.popleft()
        if cur in summits:
            continue

        for i in range(len(graph[cur])): # 다음 방문지점으로 향하는 노드를 삽입.
            next_node,next_cost = graph[cur][i] # 
            temp = max(dp[cur],next_cost) # 다음 노드로 갈때의 비용intensity, 현재 노드까지의 dp intensity중 최댓값
            if dp[next_node] > temp:  # 가지치기.
                dp[next_node] = temp # 다음노드로가는 최소 intensity
                q.append(next_node) 
    summits = list(summits)
    summits.sort()
    min_cost = 10**15
    ans = []
    for summit in summits :
        if min_cost > dp[summit]:
            min_cost = min(min_cost,dp[summit])
            ans = [summit,min_cost]
    return ans

