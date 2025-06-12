import time
import math
def time_calc(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(func.__name__,"took",round((end-start),4),"seconds")
        return result
    return wrapper
@time_calc
def calc_log(numbers):
    result = []
    for number in numbers:
        result.append(round(math.log(number),2))
    print("The log value of numbers in the ", numbers,"is",result)
    return result
a = calc_log(range(1,11))
#print(a)



