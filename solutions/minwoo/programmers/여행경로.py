
def solution(tickets):
    def dfs(node,path,ticket_cnt): 

        for i in range(len(tickets)):
            a,b = tickets[i] # a -> b 
            if visit[i] == 0 and a == node : # 다음 방문노드를 살핀다.
                visit[i] = 1
                path.append(b) # 다음방문노드
                res = dfs(b,path) 
                if len(res) == len(tickets)+1: # 모든 티켓을 사용하면, path를 바로 리턴한다.
                    return path
                path.pop()
                visit[i] = 0
        return path
        
    tickets.sort(key = lambda x : x[1])
    visit = [0]*(len(tickets))
    
    return dfs("ICN",["ICN"],0) 

