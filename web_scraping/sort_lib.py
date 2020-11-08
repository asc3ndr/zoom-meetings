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


def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] / exp1
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] / exp1
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


def min_bubble_sort(array, num):

    tider = []
    for i in range(num):
        start = timeit.default_timer()
        bubble_sort(array)
        end = timeit.default_timer()
        tider.append(end - start)

    return min(tider)


def min_radixSort(array, num):

    tider = []
    for i in range(num):
        start = timeit.default_timer()
        radixSort(array)
        end = timeit.default_timer()
        tider.append(end - start)

    return min(tider)


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


arr1 = [randint(0, 1000000) for num in range(5000)]
arr2 = [randint(0, 1000000) for num in range(10000)]
arr3 = [randint(0, 1000000) for num in range(15000)]
arr4 = [randint(0, 1000000) for num in range(20000)]
arr5 = [randint(0, 1000000) for num in range(40000)]
arr6 = [randint(0, 1000000) for num in range(80000)]
arr7 = [randint(0, 1000000) for num in range(160000)]
arr8 = [randint(0, 1000000) for num in range(320000)]
all_arr = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8]

mergesort_tider = []
quicksort_tider = []
# radixsort_tider = []
bubble_sort_tider = []

for array in all_arr:

    mergesort_tid = min_mergesort(array, 1)
    quicksort_tid = min_quicksort(array, 1)
    # radixsort_tid = min_radixSort(array, 1)
    bubble_sort_tid = min_bubble_sort(array, 1)

    mergesort_tider.append(mergesort_tid)
    quicksort_tider.append(quicksort_tid)
    # radixsort_tider.append(radixsort_tid)
    bubble_sort_tider.append(bubble_sort_tid)


print(mergesort_tider)
print(quicksort_tider)
# print(radixsort_tider)
print(bubble_sort_tider)

plt.autoscale(True)
plt.plot(
    [len(value) for index, value in enumerate(all_arr)], mergesort_tider, color="b"
)
plt.plot(
    [len(value) for index, value in enumerate(all_arr)], quicksort_tider, color="r"
)
# plt.plot(
#     [len(value) for index, value in enumerate(all_arr)], radixsort_tider, color="g"
# )
plt.plot(
    [len(value) for index, value in enumerate(all_arr)], bubble_sort_tider, color="y"
)

plt.xlabel("Datamengde")
plt.ylabel("Time in seconds")
plt.show()
