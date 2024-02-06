def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    i = j = 0
    for k in range(low, high + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        elif right[j] <= left[i]:
            arr[k] = right[j]
            j += 1
        if i == len(left):
            arr[k + 1:high + 1] = right[j:]
            break
        if j == len(right):
            arr[k + 1:high + 1] = left[i:]
            break
    return arr


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    else:
        return arr
    return arr


arr = [5, 3, 2, 8, 1]
print(merge_sort(arr, 0, len(arr) - 1))
