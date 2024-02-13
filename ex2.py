import timeit
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

array_size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]

for case in ["best", "worst", "average"]:
    bubble_times = []
    quick_times = []

    for size in array_size:
        if case == "best":
            arr = list(range(size))
        elif case == "worst":
            arr = list(range(size, 0, -1))
        elif case == "average":
            arr = random.sample(range(size), size)
        
        bubble_time = timeit.timeit(stmt='bubble_sort(arr[:])', globals=globals(), number=100)
        quick_time = timeit.timeit(stmt='quick_sort(arr[:])', globals=globals(), number=100)

        bubble_times.append(bubble_time)
        quick_times.append(quick_time)

    for alg, color, marker in [("Bubble Sort", 'red', 'o'), ("Quick Sort", 'blue', '^')]:
        plt.scatter(array_size, bubble_times if alg == "Bubble Sort" else quick_times, label=f'{alg}', color=color, marker=marker)

    better_bubble = [i for i in range(len(array_size)) if bubble_times[i] < quick_times[i]]
    plt.scatter([array_size[i] for i in better_bubble], 
                [bubble_times[i] if bubble_times[i] < quick_times[i] else quick_times[i] for i in better_bubble], 
                color='green', marker='o', label='Bubble Sort Better')
    
    better_quick = [i for i in range(len(array_size)) if bubble_times[i] > quick_times[i]]
    plt.scatter([array_size[i] for i in better_quick], 
                [bubble_times[i] if bubble_times[i] > quick_times[i] else quick_times[i] for i in better_quick], 
                color='orange', marker='^', label='Quick Sort Better')

    plt.xlabel('Array Size')
    plt.ylabel('Time (s)')
    plt.title(f'Bubble Sort vs Quick Sort ({case} case)')
    plt.legend()
    plt.show()
