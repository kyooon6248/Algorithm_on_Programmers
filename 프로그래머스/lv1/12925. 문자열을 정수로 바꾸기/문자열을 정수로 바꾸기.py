def solution(s):
    return (int(s) if '-' not in s else -1*int(s[1:]))