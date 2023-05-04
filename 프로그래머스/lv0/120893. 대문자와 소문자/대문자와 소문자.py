def solution(my_string):
    answer = []
    for a in my_string:
        if a.islower() == True:
            answer.append(a.upper())
        else:
            answer.append(a.lower())
    return ''.join(answer)