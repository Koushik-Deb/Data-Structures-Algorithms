# Worst  ---------- Best --------- Average
#  O(n^2) --------- O(n) -------- O(n^2)
# Space ? O(1)
# Stabe ? Yes
# Inplace ? Yes

def bubbleSort(arr):
    for i in range(len(arr)):
        flag = 0
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                flag = 1
                arr[j],arr[j+1] = arr[j+1], arr[j]
        if not flag:
            break
    return arr


arr=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(bubbleSort(arr))