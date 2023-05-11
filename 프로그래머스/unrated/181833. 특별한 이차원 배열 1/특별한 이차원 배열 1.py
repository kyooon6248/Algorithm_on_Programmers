def solution(n):
    answer = []
    for i in range(n):
        arr = [0 for _ in range(n-1)]
        arr.insert(i, 1)
        answer.append(arr)
    
    
    
    return answer