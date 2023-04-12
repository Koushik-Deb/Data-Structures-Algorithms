def iterativeBinarySearch(ls, key):
    lo, hi = 0, len(ls)
    index = -1

    while(lo<=hi):
        mid = (lo+hi)//2
        if ls[mid]==key:
            index = mid
            break
        elif ls[mid]>key:
            hi = mid-1
        else: 
            lo = mid+1

    return index

def recursiveBinarySearch(ls, lo, hi, key):
    if lo<=hi:
        mid = (lo+hi)//2
        if ls[mid]==key:
            return mid
        elif ls[mid]>key:
            return recursiveBinarySearch(ls, lo, mid-1, key)
        return recursiveBinarySearch(ls, mid+1, hi, key)
    return -1

if __name__=='__main__':
    n = int(input("Type the length of the array\n"))
    ls = [int(i) for i in input("Please input the sorted array like this - 1 2 5\n").split()]
    find = int(input("Input the value you want to find\n"))
    ls = [101, 7, 7,9, 10,10,15, 12, 23, 23, 34, 44, 78]
    ls.sort()
    find = 15
    n = len(ls)
    print(iterativeBinarySearch(ls, find))
    print(recursiveBinarySearch(ls, 0, n, find))
