import heapq
def solution(n, works):
    q = [-work for work in works]
    heapq.heapify(q) 
    sum = 0
    while n :
        ele = -heapq.heappop(q)
        if ele >0 : 
            ele-=1
        n-=1 
        heapq.heappush(q,-ele) 
    while q :
        ele = -heapq.heappop(q)
        sum+=ele**2
    return sum
