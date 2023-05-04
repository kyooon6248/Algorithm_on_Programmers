def solution(my_string, num1, num2):
    l = list(my_string)
    n1 = l[num1]
    n2 = l[num2]
    l[num1] = n2
    l[num2] = n1
    return ''.join(l)