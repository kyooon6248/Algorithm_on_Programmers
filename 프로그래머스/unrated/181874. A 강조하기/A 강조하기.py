def solution(myString):
    answer = ''
    for i in myString.lower():
        if i == 'a':
            answer += 'A'
        else:answer += i
    return answer