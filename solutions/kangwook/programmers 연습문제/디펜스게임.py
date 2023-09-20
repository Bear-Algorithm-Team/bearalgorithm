import heapq

def solution(n, k, enemy):
    if k >= len(enemy): return len(enemy)
    
    q = []
    for i, elem in enumerate(enemy):
        heapq.heappush(q, elem)
        if len(q) == k + 1:
            elem_to_pop = heapq.heappop(q)
            n -= elem_to_pop
            if n < 0: return i
    return len(enemy)
