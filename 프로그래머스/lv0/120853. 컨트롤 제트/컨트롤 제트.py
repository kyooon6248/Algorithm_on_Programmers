def solution(s):
    answer = 0
    temp_i = ''
    for i in s.split(' '):
        if i == 'Z':
            if (temp_i, i) == ('Z', 'Z'):
                pass
            else:
                answer -= int(temp_i)
        else:
            answer += int(i)
        temp_i = i
    return answer