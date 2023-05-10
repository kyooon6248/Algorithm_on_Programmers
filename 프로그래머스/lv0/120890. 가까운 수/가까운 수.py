def solution(array, n):
    array.append(n)
    array = sorted(array)
    if array[-1] == n:
        return array[-2]
    
    n_index = array.index(n)
    prev_index = n_index - 1
    next_index = n_index + 1
    
    prev_range = n - array[prev_index]
    next_range = array[next_index] - n
    
    if prev_range > next_range:
        return array[next_index]
    else: return array[prev_index]