n = int(input())
arr = list(map(int,input().split()))
st = []
ans = []

for i in range(n):
    if not st :
        ans.append(0)
        st.append([i+1,arr[i]])
        continue

    while st and st[-1][1] < arr[i] : # 현재수보다 작은놈은 다 뺀다.
        st.pop()
    if not st : # 다 뺐더니, 수신가능한 탑이 없을 때.
        ans.append(0)
        st.append([i+1,arr[i]])
    else: # 수신가능 탑이 있을때.
        ans.append(st[-1][0])
        st.append([i+1,arr[i]])
print(*ans)