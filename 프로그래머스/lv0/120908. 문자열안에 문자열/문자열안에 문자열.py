def solution(str1, str2):
    import re
    p = re.compile(str2)
    m = p.search(str1)
    if m == None:
        answer = 2
    else:
        answer = 1
    return answer