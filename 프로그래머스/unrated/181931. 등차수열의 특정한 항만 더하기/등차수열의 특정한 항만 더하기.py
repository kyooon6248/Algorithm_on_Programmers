def solution(a, d, included):
    return sum([i for i, b in zip(list(range(a, a+(len(included)*d), d)), included) if b])