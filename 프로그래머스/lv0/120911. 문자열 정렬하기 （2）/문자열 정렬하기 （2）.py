def solution(my_string):
    l = list(my_string.lower())
    l.sort()
    l = ''.join(l)
    return l