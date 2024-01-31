"""
GROUP 1
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

# TODO: Bucket Sort

def main():
    try:
        arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Sorted Array using Counting Sort: ", counting_sort(arr))
        # print("Sorted Array using Quick Sort: ", quick_sort(arr, 0, len(arr) - 1))
    except ValueError:
        print("Please enter only integers separated by spaces.")


if __name__ == '__main__':
    main()
