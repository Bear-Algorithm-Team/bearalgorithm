import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s,e = map(int,input().split())
    arr.append([s,1]) # 들어오는것 
    arr.append([e,0]) # 나가는것.

arr.sort(key = lambda x : (x[0],x[1])) #나가는시점,들어오는시점이 같은것은 나가는 것부터 처리해야함
cnt = 0
ans = 0
for t,inout in arr :
    if inout :
        cnt +=1
    else:
        cnt -= 1
    ans = max(ans,cnt)
print(ans)