def linearSearch(ls,key):
    for val in ls:
        if val==key:
            return str(key) + " is in the array"
    return str(key) + " is not in the array"

if __name__=='__main__':
    n = int(input("Type the length of the array\n"))
    ls = [int(i) for i in input("Please input the array like this - 1 2 5\n").split()]
    find = int(input("Input the value you want to find\n"))
    print(linearSearch(ls, find))