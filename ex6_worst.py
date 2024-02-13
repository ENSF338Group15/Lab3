import timeit
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

avg_linear_times = []
avg_binary_times = []

for size in sizes:
    total_linear_time = [] 
    total_binary_time = [] 
    
    for _ in range(100):
        arr = list(range(size, 0, -1))
        target = random.choice(arr)
        
        linear_time = timeit.timeit(lambda: linear_search(arr, target), number=1)
        total_linear_time.append(linear_time)  
        
        sorted_arr = quick_sort(arr)
        binary_time = timeit.timeit(lambda: binary_search(sorted_arr, target), number=1)
        total_binary_time.append(binary_time)  

    avg_linear_time = sum(total_linear_time) / 100
    avg_binary_time = sum(total_binary_time) / 100

    avg_linear_times.append(avg_linear_time)
    avg_binary_times.append(avg_binary_time)

plt.scatter(sizes, avg_linear_times, label='Linear Search', color='red')
plt.scatter(sizes, avg_binary_times, label='Binary Search', color='blue')
plt.xlabel('Array Size')
plt.ylabel('Average Time (s)')
plt.xscale('log')
plt.yscale('log')
plt.title('Linear vs Quick Sort(Worst Case) & Binary Search')
plt.legend()
plt.show()
