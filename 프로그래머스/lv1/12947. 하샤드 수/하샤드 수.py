def solution(x):
    str_x = list(str(x))
    summary = 0
    for i in str_x:
        summary += int(i)
    return x%summary == 0