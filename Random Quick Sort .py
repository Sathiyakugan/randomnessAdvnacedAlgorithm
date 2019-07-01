import random
import datetime
import numpy as np


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
def quick_sort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    # Create K index's array with even distribution


Number_array = [10000, 100000, 1000000]

time_duration = []
kth_value = []

for N in Number_array:
    # Get the K's value array
    k = random.sample(range(1, N), 1000)
    for i in range(1000):
        # LOW and HIGH values are setted
        low = 0
        array_random = random.sample(range(1, 100000000), N)
        high = len(array_random) - 1

        # Start timing
        start_time = datetime.datetime.now()

        quick_sort(array_random, low, high)
        kth_value.append(array_random[k[i]])

        # End time
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        time_duration.append(duration.total_seconds() * 1000)

        array_random.clear()

    print("mean time ", np.mean(time_duration), "ms")
    time_duration.clear()
    print(k)
    print(kth_value)