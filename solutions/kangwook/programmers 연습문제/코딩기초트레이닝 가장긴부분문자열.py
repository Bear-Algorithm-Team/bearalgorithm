def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]
