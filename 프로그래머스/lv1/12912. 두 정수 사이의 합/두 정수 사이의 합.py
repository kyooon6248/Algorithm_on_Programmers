def solution(a, b):
    l = []
    if a == b:
        return a
    elif a < b:
        for i in range(a, b + 1):
            l.append(i)       
        return sum(l)
    else:
        for i in range(b, a + 1):
            l.append(i)        
        return sum(l)