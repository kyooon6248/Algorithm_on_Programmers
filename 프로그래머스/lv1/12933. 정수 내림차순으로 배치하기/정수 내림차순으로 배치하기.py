def solution(n):
    l = list(str(n))
    l.sort(reverse=True)
    return int(''.join(l))
