
import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    ans = []
    max_heap = []
    min_heap = []

    for i in range((n // 10) + 1): 
        temp = list(map(int, input().split()))
        for x in temp:
            arr.append(x)

    for i in range(len(arr)) : 
        num = arr[i]
        # 두 힙의 크기를 최대 1개 차이나게 유지해야 중앙값을 뽑을 수 있다. 
        if len(max_heap) == len(min_heap) : # max_heap을 먼저 채워넣는다.
            heapq.heappush(max_heap,-num)
        else:
            heapq.heappush(min_heap, num)

        if len(min_heap) > 0 and len(max_heap)> 0 :
            if -max_heap[0] > min_heap[0] :
                # 스왑
                max_ele = -heapq.heappop(max_heap)
                min_ele = heapq.heappop(min_heap)
                heapq.heappush(min_heap,max_ele)
                heapq.heappush(max_heap,-min_ele)

        if (i+1)%2 == 1:
            ans.append(-max_heap[0])
    # 출력
    print(n//2+1)
    sliced_ans = [ans[i:i + 10] for i in range(0, len(ans), 10)]
    for ans in sliced_ans :
        print(*ans)