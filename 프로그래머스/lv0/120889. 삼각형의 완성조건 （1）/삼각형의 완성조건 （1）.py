def solution(sides):
    answer = 2
    s = sorted(sides)
    if sum(s[:2]) > s[-1]:
        answer -= 1
    return answer