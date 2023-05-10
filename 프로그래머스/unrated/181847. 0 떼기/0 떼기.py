def solution(n_str):
    if n_str[0] != '0': # 맨 앞에 0이 아닌 경우 그대로 return
        return n_str
    for i, num in enumerate(n_str): # 0부터 시작하는 경우
        if num != '0':
            return n_str[i:]