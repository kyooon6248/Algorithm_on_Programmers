def solution(cipher, code):
    answer = ''
    for i in range(len(cipher) + 1):
        if i > 0 and i % code == 0:
            answer += cipher[i - 1]
    return answer