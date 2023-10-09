from itertools import combinations_with_replacement
import heapq

def solution(k,n,reqs): 
    def solve(num_consultant_by_type):
        consultants = [[] for _ in range(k+1)] # 상담유형에 따라 큐가 다름 .
        ans = 0
        for start,duration,type in reqs :
            consultant = consultants[type] # 해당 유형의 상담사의 힙
            if len(consultant) < num_consultant_by_type[type] : # 상담사가 충분할때는 그냥 삽입. 대기시간은 없음.
                heapq.heappush(consultant, (start+duration)) # 종료시간만 삽입
                continue
            qe = heapq.heappop(consultant)

            if qe > start : # 대기시간이 발생할 때.
                ans += qe-start
                heapq.heappush(consultant, (qe+duration))
            else : #대기시간이 필요없을때
                heapq.heappush(consultant,(start+duration))
        return ans
    
    comb = combinations_with_replacement([i+1 for i in range(k)],n-k)
    ans = 10**9
    for com in comb :
        num_consultant_by_type = [1] * (k + 1) 
        num_consultant_by_type[0] = 0
        for c in com :
            num_consultant_by_type[c] +=1
        ans = min(ans,solve(num_consultant_by_type))
    return ans
