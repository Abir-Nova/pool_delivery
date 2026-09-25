import random
import time

numbers = [random.randint(1, 6000) for i in range(1000000)]

start = time.time()
numbers.sort()
print(time.time() - start)
print(numbers)