"""
GROUP 1: Anunay Amrit, Angelica Cabato, Pranav Vijay Chand, Riya Chapatwala
Riya Chapatwala, Sai Satya Jagannadh Doddipatla, Nhat Ho

Algorithm Specialists: Angelica Cabato, Nhat Ho

Dr. Shah

CPSC 535: Advanced Algorithms (Spring 2024)


Task:
- Implement the sorting algorithms: Heapsort, Quicksort, Linear Sorting,
and Medians & Order Statistics.
- Optimize and test the implemented algorithms for correctness.

"""


# TODO: Heapsort

# Quicksort

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # sorting everything to the left of the
        # pivot
        quick_sort(arr, pi + 1, high)  # sorting everything to the right of the
        # pivot


# TODO: Counting Sort

def counting_sort(arr):
    # find max value
    max_val = max(arr)

    temp_size = max_val + 1

    # initalize a temp arr to the size of the input arr + 1
    temp_arr = [0] * (temp_size)
    print(temp_arr)

    # Set temp[i] to equal the number of elements equal to i
    for i in range(len(arr)):
        temp_arr[arr[i]] = (temp_arr[arr[i]] + 1)

    # Set temp[i] to equal the number of elements less than or equal to i
    for i in range(1, temp_size):
        temp_arr[i] = (temp_arr[i] + temp_arr[i - 1])
        print(temp_arr[i])

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

# TODO: Radix Sort


# Insertion Sort - > helper for Bucket Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# TODO: Bucket Sort

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
        print(temp_arr[i])

    # concatenate each element from each bucket in order
    idx = 0
    for i in range(len(arr)):
        for j in range(len(temp_arr[i])):
            temp = temp_arr[i][j]
            sorted_arr[idx] = temp
            idx += 1

    return sorted_arr

def main():
    try:
        # arr = list(map(int, input("Enter numbers separated by
        # spaces:").split()))
        arr = [42, 32, 33, 52, 37, 47, 51]
        # arr = [.42, .32, .33, .52, .37, .47, .51]
        # print("Sorted Array using Counting Sort: ", counting_sort(arr))
        # print("Sorted Array using Quick Sort: ", quick_sort(arr, 0, len(arr) - 1))
        print("Sorted Array using Bucket Sort: ", bucket_sort(arr))
    except ValueError:
        print("Please enter only integers separated by spaces.")


if __name__ == '__main__':
    main()
