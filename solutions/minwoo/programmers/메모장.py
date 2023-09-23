
def solution(K, words):
    line = 1
    temp = ""
    for word in words :
        if temp == "":
            temp = word
        else:
            temp += " "+word
        
        if len(temp) > K :
            line +=1
            temp = word
    return line