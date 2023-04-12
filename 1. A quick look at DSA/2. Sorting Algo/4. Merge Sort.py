# Worst  ---------- Best --------- Average
#  O(nlogn) --------- O(nlogn) -------- O(nlogn)
# Space ? O(n)
# Stabe ? Yes
# Inplace ? No


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)
    
def merge(arr, left, right):
    i, j, k = 0,0,0
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while(i<len(left)):
        arr[k] = left[i]
        k+=1
        i+=1
    while(j<len(right)):
        arr[k] = right[j]
        k+=1
        j+=1

a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
mergeSort(a)
print(*a, sep=" ")