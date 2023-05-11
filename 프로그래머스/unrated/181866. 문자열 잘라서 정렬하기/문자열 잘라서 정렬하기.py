def solution(myString):
    l = sorted([i for i in myString.split('x')])
    return list(filter(None, l))