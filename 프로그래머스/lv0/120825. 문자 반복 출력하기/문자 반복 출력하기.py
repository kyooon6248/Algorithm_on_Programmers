def solution(my_string, n):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i] * n)
    return ''.join(answer)