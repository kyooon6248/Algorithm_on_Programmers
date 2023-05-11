def solution(num):
    if num == 1:
        return 0
    for count in range(500):
        if num%2==0:
            num = num//2
        else:
            num = 3*num+1
        if num==1:
            return count+1
    return -1