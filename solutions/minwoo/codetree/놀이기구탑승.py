from collections import defaultdict
n = int(input())
_map = defaultdict(set)
ans = 0
board = [[0]*n for _ in range(n)]

for i in range(n**2):
    arr = list(map(int,input().split()))
    for key in arr[1:]:
        _map[arr[0]].add(key)

def step1():
    for k,_set in _map.items() : # k 를 앉혀야함.
        positions = [] # k가 앉을수있는 후보들 
        for i in range(n):
            for j in range(n):
                if board[i][j]:
                    continue
                friends = 0
                empty = 0
                for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                    ny = i+dy
                    nx = j+dx
                    if 0<=ny<n and 0<=nx<n :
                        if board[ny][nx] in _set:
                            friends+=1
                        if board[ny][nx] == 0 :
                            empty+=1
                positions.append([friends,empty,i,j]) # 후보삽입 .
        positions.sort(key = lambda x : (-x[0],-x[1],x[2],x[3]))
        friends, empty, i, j= positions[0]
        board[i][j] = k

def calc_score():
    ans = 0
    for i in range(n):
        for j in range(n):
            friends = 0
            for dy,dx in ((0,1),(0,-1),(1,0),(-1,0)):
                ny,nx = dy+i,dx+j
                if not(0<=ny<n and 0<=nx<n): continue
                if board[ny][nx] in _map[board[i][j]] :
                    friends+=1
            ans += int(10**(friends-1))
    return ans
step1()
print(calc_score())