import math 
import time 

#math.pow function 
t0 = time.perf_counter()

math.pow(2, 2)

t1 = time.perf_counter()

2**2

t2 = time.perf_counter()

math_pow = t1 - t0
print("first test took " ,math_pow, "milli seconds")
regular_exponet = t2 - t1 
print("second test took " ,math_pow, "milli seconds")


start_time = time.process_time()
a = 2**2
print(a)
end_time = time.process_time()
print("It took " ,(end_time - start_time), " seconds")

