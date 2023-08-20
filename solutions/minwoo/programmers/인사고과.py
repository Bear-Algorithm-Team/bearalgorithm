# 앞에 순차탐색하면서, 최솟값을 갱신한다. 
# 최솟값 보단 커야 한다. 

def solution(scores):
    # 정렬하고 석차에 들어갈수잇는애인지 표시한다.
    for i in range(len(scores)):
        if i == 0 :
            scores[i] = [scores[i][0],scores[i][1],"Y"] # 완호 표시
        else:
            scores[i] = [scores[i][0],scores[i][1],"N"] 
    scores.sort(key = lambda x:(-x[0],x[1]))
    max_score = 0
    temp = []
    for score in scores:
        if max_score <= score[1]:
            temp.append(score)
        max_score = max(max_score,score[1])
    scores = temp
    
    scores.sort(key = lambda x : -(x[0]+x[1]))
    ans = 1
    flag = False
    for i in range(len(scores)):
        if scores[i][2] == 'Y':
            return ans 
        else:
            ans+=1
    if flag : 
        return ans 
    else:
        return -1
        