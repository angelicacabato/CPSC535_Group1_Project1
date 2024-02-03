"""
GROUP 1: Anunay Amrit, Angelica Cabato, Pranav Vijay Chand, Riya Chapatwala
Riya Chapatwala, Sai Satya Jagannadh Doddipatla, Nhat Ho

Algorithm Specialists: Angelica Cabato, Nhat Ho

Dr. Shah

CPSC 535: Advanced Algorithms (Spring 2024)


Task:
- Implement the sorting algorithms: Bubble Sort, Insertion Sort, Merge Sort,
Heap Sort,
Quick Sort,
Counting Sort, Radix Sort, Bucket Sort, and Medians & Order Statistics.
- Optimize and test the implemented algorithms for correctness.

"""
import multiprocessing
import time
import numpy as np
import matplotlib.pyplot as plt

################### Bubble Sort ########################
# TODO: Bubble Sort

######################################################

################### Merge Sort ########################
# TODO: Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array into left and right sections
        L = arr[:mid]
        R = arr[mid:]

        # Sorting each half of the array
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copying elements over
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking for any elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr
######################################################

################### Heap Sort ########################
def build_max_heap(arr, n, i):
    root = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[root]:
        root = left
    
    if right < n and arr[right] > arr[root]:
        root = right

    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        build_max_heap(arr, n, root)

def heap_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len // 2-1, -1, -1):
        build_max_heap(arr, arr_len, i)

    for i in range(arr_len-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        build_max_heap(arr, i, 0)

    return arr
######################################################

################### Quick Sort #######################
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def run_quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        run_quick_sort(arr, low, pi - 1)  # sorting everything to the left of the
        # pivot
        run_quick_sort(arr, pi + 1, high)  # sorting everything to the right of the
        # pivot

def quick_sort(arr):
    run_quick_sort(arr, 0, len(arr) - 1)
    return arr
######################################################

################### Counting Sort ####################   
def counting_sort(arr):
    # find max value
    max_val = max(arr)

    temp_size = max_val + 1

    # initalize a temp arr to the size of the input arr + 1
    temp_arr = [0] * (temp_size)

    # Set temp[i] to equal the number of elements equal to i
    for i in range(len(arr)):
        temp_arr[arr[i]] = (temp_arr[arr[i]] + 1)

    # Set temp[i] to equal the number of elements less than or equal to i
    for i in range(1, temp_size):
        temp_arr[i] = (temp_arr[i] + temp_arr[i - 1])

    # create sorted array and initialize to 0
    sorted_arr = [0] * (len(arr))

    # sort the list and transfer to sorted array
    i = (len(arr) - 1)
    while i >= 0:
        sorted_arr[temp_arr[arr[i]] - 1] = arr[i]
        temp_arr[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, len(arr)):
        arr[i] = sorted_arr[i]

    return arr
######################################################

################### Radix Sort #######################
def counting_sort_helps_radix(arr, exp):
 
    arr_len = len(arr)
    # declare the output array
    output = [0] * (arr_len)
    # initialize array having 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, arr_len):
        index = arr[i] // exp
        modulo = index % 10
        count[modulo] += 1
 
    # Get actual position of current digit
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = arr_len - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
 
    # Get the sorted array
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
 
def radix_sort(arr):
    # Find the maximum number
    max_num = max(arr)
    exp = 1
    while max_num // exp >= 1:
        counting_sort_helps_radix(arr, exp)
        exp *= 10
    return arr
######################################################

################### Insertion Sort ######################
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
######################################################

################### Bucket Sort ######################
def bucket_sort(arr):
    temp_arr = []

    # create sorted array and initialize to 0
    sorted_arr = [0] * (len(arr))

    # find max value to determine bucket size
    max_value = max(arr)
    size = max_value / len(arr)

    # create buckets
    for i in range(len(arr)):
        temp_arr.append([])

    # insert elements into buckets
    for i in range(len(arr)):
        idx = int(arr[i] / size)
        if idx != len(arr):
            temp_arr[idx].append(arr[i])
        else:
            temp_arr[len(arr) - 1].append(arr[i])


    # Sort buckets with insertion sort
    for i in range(len(arr)):
        temp_arr[i] = insertion_sort(temp_arr[i])

    # concatenate each element from each bucket in order
    idx = 0
    for i in range(len(arr)):
        for j in range(len(temp_arr[i])):
            temp = temp_arr[i][j]
            sorted_arr[idx] = temp
            idx += 1

    return sorted_arr
######################################################

def get_time(algo, arr):
    start_time = time.time()
    algo(arr)
    end_time = time.time()
    return end_time - start_time

def run_algorithm(algoes, arr):
    pool = multiprocessing.Pool(processes=len(algoes))
    time_results = []

    for algo in algoes:
        result = pool.apply_async(get_time, (algo, arr.copy()))
        time_results.append(result)

    times = [float(result.get()) for result in time_results]
    return times

def main():
    try:
        # arr = list(map(int, input("Enter numbers separated by
        # spaces:").split()))
        arr = [4, 19, 35, 64, 22, 0, 57, 82, 12, 55, 89, 34, 567, 78, 123, 456]
        # print("Sorted Array using Counting Sort: ", counting_sort(arr))
        # print("Sorted Array using Quick Sort: ", quick_sort(arr))
        # print("Sorted Array using Bucket Sort: ", bucket_sort(arr))
        # print("Sorted Array using Heap Sort: ", heap_sort(arr))
        # print("Sorted Array using Radix Sort: ", radix_sort(arr))
        # print("Sorted Array using Merge Sort: ", merge_sort(arr))


        np.random.seed(55)
        arr = list(np.random.randint(0, 1000, size=100000))

        arr_algorithms = [bucket_sort, heap_sort, radix_sort, counting_sort,
                          quick_sort, merge_sort]
        exe_times = run_algorithm(arr_algorithms, arr)

        for algorithm, time_consume in zip(arr_algorithms, exe_times):
            print(f"{algorithm.__name__} Time: {time_consume:.6f} seconds")

        # Plot the results with colors
        colors = ['blue', 'green', 'red', 'yellow', 'orange']

        for i, (algorithm, time_consume) in enumerate(zip(arr_algorithms, exe_times)):
            plt.bar(algorithm.__name__, time_consume, color=colors[i], edgecolor='black', label=algorithm.__name__, hatch='/', alpha=0.7)
        
        plt.ylabel('Time (seconds)')
        plt.title('Efficiency of Sorting Algorithms')
        plt.legend()
        plt.show()


    except ValueError:
        print("Please enter only integers separated by spaces.")
        

if __name__ == '__main__':
    main()