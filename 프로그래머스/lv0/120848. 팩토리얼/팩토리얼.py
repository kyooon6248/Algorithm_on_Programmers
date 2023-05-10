def solution(n):
    num = 1
    factorial = 0
    while n >= num:
        factorial += 1
        num = num * factorial
    return factorial-1