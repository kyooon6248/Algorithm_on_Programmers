def solution(arr, idx):
    for i, num in enumerate(arr[idx:]):
        if num == 1:
            return i + idx
    return -1