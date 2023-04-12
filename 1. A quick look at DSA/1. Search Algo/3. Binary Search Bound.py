def lowerBoundBinarySearch(ls, key):
    lo, hi = 0, len(ls)
    index = -1

    while(lo<=hi):
        mid = (lo+hi)//2
        if ls[mid]==key:
            index = mid
            hi = mid-1
        elif ls[mid]>key:
            hi = mid-1
        else:
            lo = mid+1
    return lo


def higherBoundBinarySearch(ls, key):
    lo, hi = 0, len(ls)
    index = -1

    while(lo<=hi):
        mid = (lo+hi)//2
        if ls[mid]==key:
            index = mid
            lo = mid+1
        elif ls[mid]>key:
            hi = mid-1
        else:
            lo = mid+1
    return lo

if __name__=='__main__':
    # n = int(input("Type the length of the array\n"))
    # ls = [int(i) for i in input("Please input the sorted array like this - 1 2 5\n").split()]
    # find = int(input("Input the value you want to find\n"))
    ls = [101, 7, 7,9, 10,10,15, 12, 23, 23, 34, 44, 78]
    ls.sort()
    print(ls)
    find = 15
    n = len(ls)
    print(lowerBoundBinarySearch(ls, find))
    print(higherBoundBinarySearch(ls, find))
