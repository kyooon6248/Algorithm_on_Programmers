def solution(hp):
    count = 0
    a = hp // 5
    b = hp % 5
    count = count + a
    a = b // 3
    b = b % 3
    count = count + a + b
    return count