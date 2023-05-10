def solution(todo_list, finished):
    answer = []
    for i, b in enumerate(finished):
        if int(b) == 0:
            answer.append(todo_list[i])
    return answer