import random


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return arr, comparisons, swaps

# Testing
for i in range(1, 11):
    arr = [random.randint(1, 100) for _ in range(i * 10)]
    sorted_arr, comparisons, swaps = bubble_sort(arr)
    print(f"Array size: {len(arr)}")
    print(f"Number of comparisons: {comparisons}")
    print(f"Number of swaps: {swaps}")
    print("-----------------------------")