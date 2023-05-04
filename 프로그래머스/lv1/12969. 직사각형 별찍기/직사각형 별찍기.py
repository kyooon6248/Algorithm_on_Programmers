a, b = map(int, input().strip().split(' '))
# solution 1 : for문 사용    
# for i in range(b):
#     print('*' * a)

# solution 2 : for문 안 사용

#a개를 b줄
print((('*'*a)+'\n')*b)