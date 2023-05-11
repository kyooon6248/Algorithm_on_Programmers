def solution(array):
    # arr에 동일한 값만 들어갈때 처리
    if len(array)==1: # 하나일 경우 처리
        return array[0]
    c = dict(zip(array, [0 for _ in range(len(array))]))
    for i in array:
        c[i] += 1
    sorted_c = sorted(c.items(), key=lambda x:x[1])
    
    if sorted_c[-1] == sorted_c[0]:
        return sorted_c[0][0]
    
    
    if sorted_c[-1][-1] == sorted_c[-2][-1]: # 복수일 경우 -1 출력
        return -1
    else:
        return sorted_c[-1][0]