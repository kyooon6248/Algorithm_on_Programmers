def solution(my_string):
    answer = 0
    for i in list(my_string):
        try:
            answer += int(i)
        except: pass
    return answer