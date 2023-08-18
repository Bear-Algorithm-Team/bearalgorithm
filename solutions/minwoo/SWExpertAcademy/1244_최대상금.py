t = int(input())

for tc in range(1,t+1) :
    s, k = input().split()
    set_s = set([s]) # 시작 원소를 담음.
    set_temp = set() # 각 라운드(교환횟수) 마다 set_temp에 결과값을 삽입할것임.
    ans = 0
    for _ in range(int(k)):
        while len(set_s) > 0 :
            target = list(set_s.pop())
            for i in range(len(target)-1):
                for j in range(i+1,len(target)) :
                    target[i],target[j] = target[j],target[i]
                    set_temp.add(''.join(target))
                    target[i], target[j] = target[j], target[i]
        set_s,set_temp = set_temp,set() # 다음 라운드를 위해 set_temp는 초기화 해야함.
    print(f'#{tc} {max(map(int,set_s))}')