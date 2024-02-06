import timeit
import requests
import json
import matplotlib.pyplot as plt

def binary_search(arr, x, first_midpoint_ratio):
    low = 0
    high = len(arr) - 1
    mid = int(low + first_midpoint_ratio * (high - low))

    while low <= high:
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
        mid = (high + low) // 2

    return -1

# Fetch the data
response = requests.get('https://raw.githubusercontent.com/ldkteaches-calgary/ensf338W24/main/lab03/ex7data.json')
data = json.loads(response.text)

response = requests.get('https://raw.githubusercontent.com/ldkteaches-calgary/ensf338W24/main/lab03/ex7tasks.json')
tasks = json.loads(response.text)

# For each task, try different midpoints and measure the time taken
best_midpoints = []

for task in tasks:
    best_time = float('inf')
    best_midpoint = None

    for midpoint in [i * 0.1 for i in range(1, 10)]:
        elapsed_time = timeit.timeit(lambda: binary_search(data, task, midpoint), number=100)
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = midpoint

    best_midpoints.append(best_midpoint)

# Plot the tasks and the corresponding best midpoints
plt.scatter(tasks, best_midpoints)
plt.xlabel('Task')
plt.ylabel('Best Midpoint')
plt.show()

'''
There appears to be a correlation between performance and choice of initial midpoint. When examining the graph,
some tasks have data concentrated more depending on the chosen midpoint. I believe this is due to the nature of
the data, if the chosen midpoint reflects the data more accurately, a fewer number of iterations will be required
to find the target value. However if it is not accurate, the performance will degrade.
'''