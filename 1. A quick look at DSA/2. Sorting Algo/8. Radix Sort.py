# Worst  ---------- Best --------- Average
#  O(n+k) --------- O(n+k) -------- O(n+k)
# Space ? O(max)
# Stabe ? Yes
# Inplace ? No

def countingSort(arr, place):
    aux = [0]*(10)
    result = [0]*len(arr)
    
    for val in arr:
        aux[(val//place)%10]+=1
    for i in range(1,10):
        aux[i]+=aux[i-1]
    for val in arr[::-1]:
        index = val//place
        aux[index%10] -= 1
        result[aux[index%10]] = val
    
    return result


def radixSort(arr):
    maximum = max(arr)
    place = 1

    while(maximum//place>0):
        arr = countingSort(arr, place)
        place *= 10
    return arr
a=[10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print(radixSort(a))
