def solution(numLog):
    d = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    return ''.join([d[numLog[i+1]-numLog[i]] for i in range(0, len(numLog)-1)])