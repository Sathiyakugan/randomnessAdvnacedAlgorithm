import random
from random import randrange
import datetime
import numpy as np


def partition(x, pivot_index=0):
    i = 0
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            i += 1
    x[0], x[i] = x[i], x[0]
    return x, i


def RSelect(x, k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x, randrange(len(x)))
        x = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j], k)
        else:
            k = k - j - 1
            return RSelect(x[(j + 1):], k)


Number_array = [10000, 100000, 1000000]
time_duration = []
kth_value = []

for N in Number_array:
    k = random.sample(range(1, N), 1000)
    for i in range(1000):
        # LOW and HIGH values are setted
        low = 0
        array_random = random.sample(range(1, 10000000), N)
        high = len(array_random) - 1

        # Start timing
        start_time = datetime.datetime.now()

        k_value = RSelect(array_random, k[i])
        kth_value.append(k_value)

        # End time
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        time_duration.append(duration.total_seconds() * 1000)

        array_random.clear()

    print("mean time for  " + str(N) + ": ", np.mean(time_duration), "ms")
    print(k)
    print(kth_value)
    print(time_duration)
