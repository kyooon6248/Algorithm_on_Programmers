def solution(i, j, k):
    answer = 0
    for i in list(range(i, j+1)):
        for j in list(str(i)):
            if str(k) == j :
                answer += 1
    return answer