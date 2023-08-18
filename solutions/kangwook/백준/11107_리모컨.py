answer = 0x3f3f3f3f
N = int(input())
M = int(input())
broken = list(map(int, input().split(' '))) if M > 0 else []
buttons = [i for i in range(10) if i not in broken]
answer = abs(100 - N)

if M == 10:
    print(answer)
    exit(0)

def find(num):
    global answer

    if num != '':
        answer = min(answer, abs(N - int(num)) + len(num))
    
    if len(num) == 6:
        return
    
    for btn in buttons:
        find(num + str(btn))

find('')
print(answer)
