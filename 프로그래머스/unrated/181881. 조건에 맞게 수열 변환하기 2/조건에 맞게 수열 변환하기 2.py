def solution(arr):
    x = 0
    while True:
        prev_arr = arr.copy()
        for i, num in enumerate(arr): # 값 바꿔주기
            if num>=50 and num%2==0:
                arr[i] = num//2
            elif num<50 and num%2==1:
                arr[i] = 2*num+1
        if arr == prev_arr:
            return x
        x += 1