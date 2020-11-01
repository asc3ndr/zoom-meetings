import timeit
import matplotlib.pyplot as plt
from json import load
from random import randint


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)


def min_mergesort(array, num):

    tider = []
    for i in range(num):
        start = timeit.default_timer()
        n = len(array)
        mergeSort(array, 0, n - 1)
        end = timeit.default_timer()
        tider.append(end - start)

    return min(tider)


def min_quicksort(array, num):

    tider = []
    for i in range(num):
        start = timeit.default_timer()
        quicksort(array)
        end = timeit.default_timer()
        tider.append(end - start)

    return min(tider)


arr1 = [randint(0, 100) for num in range(500)]
arr2 = [randint(0, 100) for num in range(1000)]
arr3 = [randint(0, 100) for num in range(1500)]
arr4 = [randint(0, 100) for num in range(2000)]
all_arr = [arr1, arr2, arr3, arr4]

mergesort_tider = []
quicksort_tider = []

for array in all_arr:

    mergesort_tid = min_mergesort(array, 100)
    quicksort_tid = min_quicksort(array, 100)

    mergesort_tider.append(mergesort_tid)
    quicksort_tider.append(quicksort_tid)


plt.autoscale(True)
plt.plot(
    [len(value) for index, value in enumerate(all_arr)], mergesort_tider, color="b"
)
plt.plot(
    [len(value) for index, value in enumerate(all_arr)], quicksort_tider, color="r"
)

plt.xlabel("Datamengde")
plt.ylabel("Time in seconds")
plt.show()
