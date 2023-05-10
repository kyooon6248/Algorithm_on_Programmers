def solution(binomial):
    l = list(binomial.split(' '))
    sign = l[1]
    num1 = int(l[0])
    num2 = int(l[-1])
    if sign == '+':
        return num1+num2
    elif sign == '-':
        return num1-num2
    else:
        return num1*num2