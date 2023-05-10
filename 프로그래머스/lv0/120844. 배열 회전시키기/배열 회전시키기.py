def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0, numbers.pop(-1))
    else:
        numbers.append(numbers.pop(0))
    return numbers