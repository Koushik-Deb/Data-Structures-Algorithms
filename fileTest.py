# file1 = open("file.text","a+")
# lines = ["[1 2 3]\n","3"]
# file1.writelines(lines)
# file1.close()


with open("file.txt", 'r') as reader:
    # ls = print(reader.read(), end="\n")
    ls = reader.readlines()
    print(ls)