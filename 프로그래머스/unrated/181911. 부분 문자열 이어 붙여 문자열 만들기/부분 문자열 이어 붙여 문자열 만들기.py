def solution(my_strings, parts):
    answer = ''
    for s, i in zip(my_strings, parts):
        answer += s[i[0]:i[1]+1]
    return answer