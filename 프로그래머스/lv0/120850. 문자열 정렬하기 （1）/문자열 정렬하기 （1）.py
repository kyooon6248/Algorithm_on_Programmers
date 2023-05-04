def solution(my_string):
    answer = []
    my_string = list(my_string)
    for i in my_string:
        if i.isdecimal():
            answer.append(int(i))
        else:
            pass
    answer.sort()
    return answer