def solution(picks, minerals):
    material_map = {
        'diamond': {
            'diamond':1,
            'iron':1,
            'stone':1
        },
        'iron':{
            'diamond':5,
            'iron':1,
            'stone':1
        },
        'stone': {
            'diamond':25,
            'iron':5,
            'stone':1
        }
    }
    pick_map = {
        0:'diamond',
        1:'iron',
        2:'stone'
    }

    def calc_effort(pick, mineral_group):
        return sum(material_map[pick][mineral] for mineral in mineral_group)

    listed_picks = [] # 작은 피로도를 사용하는 곡괭이부터, 사용가능한 개수만큼 이를 나열한 리스트
    for i, pick in enumerate(picks): 
        listed_picks += [pick_map[i] for _ in range(pick)]

    mineral_groups = [] # 광물들을 5개 크기 버켓으로 잘라서 저장한 리스트
    for i in range(0, len(minerals), 5):
        mineral_groups += [minerals[i:i+5]]
        if len(mineral_groups) == len(listed_picks):
            break

    # 돌 곡괭이를 사용하는 경우 높은 피로도가 드는 버켓부터 내림차순 정렬. 이렇게 하면, 높은 피로도가 드는 버켓부터 작은 피로도를 사용하는 곡괭이를 사용하게 하면 된다.
    mineral_groups.sort(key = lambda x: -calc_effort('stone', x)) 

    answer = 0
    for pick, mineral_group in zip(listed_picks[:len(mineral_groups)], mineral_groups):
        answer += calc_effort(pick, mineral_group)
    return answer

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
