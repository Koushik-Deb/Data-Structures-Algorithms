# Worst  ---------- Best --------- Average
#  O(n^2) --------- O(nlogn) -------- O(nlogn)
# Space ? O(logn)
# Stabe ? No
# Inplace ? Yes

def partition(arr,lo, hi):
    i = lo - 1
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[hi] = arr[hi],arr[i+1]
    return i+1

def quickSort(arr,lo, hi):
    if lo<hi:
        pivot = partition(arr, lo, hi)
        quickSort(arr, lo, pivot-1)
        quickSort(arr, pivot+1, hi)

a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
quickSort(a,0,len(a)-1)
print(*a,sep=" ")

