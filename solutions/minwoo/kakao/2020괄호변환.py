def check_valid(string):
    st = []
    for str in string :
        if len(st) < 1 :
            st.append(str)
        elif str == '(' :
            st.append(str)
        elif str == ')' and st[-1] == '(':
            st.pop() 
    if not len(st) :
        return True
    return False


def find_balance_index(string):
    open,close = 0,0
    for i in range(len(string)) :
        if string[i] == '(':
            open+=1
        else:
            close+=1
        if open == close :
            return i

def reverse_str(string):
    temp = ""
    for str in string : 
        if str == '(':
            temp+=')'
        else:
            temp+='('
    return temp

def solution(str):
    
    if str == "":
        return str
    
    idx = find_balance_index(str)
    u,v =  str[0:idx+1] , str[idx+1:]
    if check_valid(u):
        return u + solution(v)
    else:
        return '(' +solution(v) + ')' + reverse_str(u[1:-1])
