def solution(array, commands):
    answer = []
    for command in commands:
        temp = sorted(array[command[0]-1:command[1]])
        answer.append(temp[command[-1]-1])
    return answer