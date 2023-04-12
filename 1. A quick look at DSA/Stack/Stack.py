class Stack:
    def __init__(self,capacity):
        self.__stack = []
        self.capacity = capacity

    def isEmpty(self):
        return len(self.__stack)==0

    def isFull(self):
        return len(self.__stack)==self.capacity

    def peek(self):
        return -1 if self.isEmpty() else self.__stack[-1]

    def push(self,data):
        if self.isFull():
            return False
        self.__stack.append(data)
        return True

    def pop(self):
        return -1 if self.isEmpty() else self.__stack.pop()

    def display(self):
        print(*self.__stack,sep=" ")
st = Stack(3)

print(st.peek())
print(st.push(5))
print(st.push(2))
print(st.push(3))
print(st.push(1))

st.display()

for i in range(4):
    print(st.pop())

print(st.display())