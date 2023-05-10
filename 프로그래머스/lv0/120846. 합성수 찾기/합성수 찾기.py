def solution(n):
    answer = 0
    for i in range(3, n+1):
        count = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                if count == 0:
                    answer += 1
                    count += 1
    return answer