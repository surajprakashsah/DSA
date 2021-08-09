# Python3 program to sort an array using
# merge sort such that merge operation
# takes O(1) extra space.
def merge(arr, beg, mid, end, maxele):
    i = beg
    j = mid + 1
    k = beg

    while (i <= mid and j <= end):
        if (arr[i] % maxele <= arr[j] % maxele):
            arr[k] = arr[k] + (arr[i] % maxele) * maxele
            k += 1
            i += 1
        else:
            arr[k] = arr[k] + (arr[j] %
                               maxele) * maxele
            k += 1
            j += 1

    while (i <= mid):
        arr[k] = arr[k] + (arr[i] %
                           maxele) * maxele
        k += 1
        i += 1
    while (j <= end):
        arr[k] = arr[k] + (arr[j] %
                           maxele) * maxele
        k += 1
        j += 1

    # Obtaining actual values
    for i in range(beg, end + 1):
        arr[i] = arr[i] // maxele


# Recursive merge sort with extra
# parameter, naxele
def mergeSortRec(arr, beg, end, maxele):
    if (beg < end):
        mid = (beg + end) // 2
        mergeSortRec(arr, beg, mid, maxele)
        mergeSortRec(arr, mid + 1, end, maxele)
        merge(arr, beg, mid, end, maxele)


# This functions finds max element and
# calls recursive merge sort.
def mergeSort(arr, n):

    maxele = max(arr) + 1
    mergeSortRec(arr, 0, n - 1, maxele)

# Driver Code
if __name__ == '__main__':

    arr = [25,1,3,0,5,8,9,7,88,2,33,11,7,44]
    n = len(arr)
    mergeSort(arr, n)

    print("Sorted array")

    for i in range(n):
        print(arr[i], end=" ")


