# Worst  ---------- Best --------- Average
#  O(n^2) --------- O(n+k) -------- O(n)
# Space ? O(n+k)
# Stabe ? Yes
# Inplace ? No



def bucketSort(array,n):
    bucket = []
    for i in range(10):
        bucket.append([])
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    print(bucket)
    for i in range(10):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(10):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

if __name__ == "__main__":
    # n = int(input("Please enter the length of the array to be sorted: "))
    # print(("Enter the array with spaces, like (10 12 3 4 11)"))
    # arr = [float(i) for i in input().split()]
    arr = [ .37, .47, .51,.42, .32, .33, .52]
    n = len(arr)
    print("Before Bucket Sort ", arr)
    bucketSort(arr,n)
    print("After Bucket Sort ", arr)

#.42 .32 .33 .52 .37 .47 .51