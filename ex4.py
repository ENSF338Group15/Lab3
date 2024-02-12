import sys
import time
from matplotlib import pyplot as plt
from ex2 import quick_sort
sys.setrecursionlimit(20000)

# sizes = range(10, 10000, 1000)
sizes = range(10, 10000, 100)
times = []

for size in sizes:
    arr = [i for i in range(size, 0, -1)]
    start_time = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end_time = time.time()
    times.append(end_time - start_time)

for size, t in zip(sizes, times):
    plt.scatter(size, t, color='blue')
    print(f"Size: {size}, Time: {t}")
plt.xlabel('Array size')
plt.ylabel('Time (s)')
plt.title('Quick sort')
plt.savefig('ex4.png')
plt.show()
