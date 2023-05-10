def solution(before, after):
    answer = ''
    before = list(before)
    for a in list(after):
        if a in before:
            answer += a
            before.remove(a)
    return int(answer==after)