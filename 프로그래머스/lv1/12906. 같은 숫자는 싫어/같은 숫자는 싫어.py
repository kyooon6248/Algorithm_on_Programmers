def solution(arr):
    prev = arr[0]
    l = [arr[0]]
    for i in arr:
        try:
            if i != prev:
                l.append(i)
        except:
            pass
        prev = i
    return l