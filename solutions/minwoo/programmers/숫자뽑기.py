def solution(arr, K): 
    arr.sort()
    ans = 10**4
    for i in range(K-1,len(arr)): 
        ans = min(ans,arr[i]-arr[i-K+1])
    return ans
solution([9, 11, 9, 6, 4, 19],4)