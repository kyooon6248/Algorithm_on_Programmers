def solution(n):
    answer = [n]
    while True:
        if n == 1:
            return answer
        if n % 2 == 0: # 짝수라면
            n /= 2
            answer.append(n)
            continue
        else: # 홀수라면
            n = 3*n+1
            answer.append(n)
            continue
            
    
    
    
    return answer