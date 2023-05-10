def solution(arr):
    X = []
    for i in arr:
        for _ in range(i):
            X.append(i)
    return X