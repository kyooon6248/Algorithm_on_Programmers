def solution(n, k):
    answer = 0
    if n == 0:
        pass
    else:
        x = n // 10
    p = n * 12000 + k * 2000
    answer = p - (x * 2000)
    return answer