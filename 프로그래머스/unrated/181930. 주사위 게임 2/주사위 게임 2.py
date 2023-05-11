def solution(a, b, c):
    nums = [a, b, c]
    if len(set(nums))==1:
        return sum(nums)*sum([i*i for i in nums])*sum([i*i*i for i in nums])
    elif len(set(nums))==2:
        return sum(nums)*sum([i*i for i in nums])
    else:
        return sum(nums)
        