# Worst  ---------- Best --------- Average
#  O(n^2) --------- O(n) -------- O(n^2)
# Space ? O(1)
# Stabe ? Yes
# Inplace ? Yes


def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(insertionSort(arr))