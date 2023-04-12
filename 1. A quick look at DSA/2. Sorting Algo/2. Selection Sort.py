# Worst  ---------- Best --------- Average
#  O(n^2) --------- O(n^2) -------- O(n^2)
# Space ? O(1)
# Stabe ? No, but can be made stable
# Inplace ? Yes

def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex = j
        
        arr[minIndex],arr[i] = arr[i], arr[minIndex]
    return arr

def stableSelectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        for j in range(minIndex-1,i-1,-1):
            arr[j+1] = arr[j]
        arr[i] = temp



arr=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(selectionSort(arr))