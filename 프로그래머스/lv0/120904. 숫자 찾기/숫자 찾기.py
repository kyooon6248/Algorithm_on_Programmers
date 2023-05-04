def solution(num, k):
    l = list(str(num))
    answer = -1
    for i, n in enumerate(l):
        if int(n) == k:
            if answer != -1:
                break
            else:
                answer = i + 1
    return answer