from functools import reduce
import numpy as np
def solution(num_list):
    return int(reduce(lambda x, y : x * y, num_list) < np.power(sum(num_list), 2))