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

# TODO: Linear Sorting


def main():

    try:
        arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
        quick_sort(arr, 0, len(arr) - 1)
        print("Sorted Array: ", arr)
    except ValueError:
        print("Please enter only integers separated by spaces.")


if __name__ == '__main__':
    main()
