"""Answer to question 4
Binary insertion sort is slower than insertion sort. The worst
case of both are O(n^2), but binary insertion sort uses too
many recursion calls and became slower than insertions sort.
"""

import random
from matplotlib import pyplot as plt
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        i -= 1
        while i >= 0 and key < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


arr = [random.randint(0, 10000000) for i in range(1003)]
for i in range(3, 200):
    arr_ = arr[:i]
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr_), number=100)
    binary_insertion_sort_time = timeit.timeit(lambda: binary_insertion_sort(arr_), number=100)
    plt.scatter(i, insertion_sort_time, color='red')
    plt.scatter(i, binary_insertion_sort_time, color='blue')
plt.xlabel('Array size')
plt.ylabel('Time (s)')
plt.title('Insertion sort vs binary insertion sort')
plt.legend(['Insertion sort', 'Binary insertion sort'])
plt.savefig('ex5.png')
plt.show()
