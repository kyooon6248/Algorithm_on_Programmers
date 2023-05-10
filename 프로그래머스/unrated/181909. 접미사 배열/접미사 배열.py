def solution(my_string):
    return sorted([my_string[i:] for i in range(0, len(my_string))])