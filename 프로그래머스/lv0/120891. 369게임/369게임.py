def solution(order):
    return sum([int(int(i) in [3, 6, 9]) for i in list(str(order))])
    