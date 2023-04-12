# Worst  ---------- Best --------- Average
#  O(nlogn) --------- O(nlogn) -------- O(nlogn)
# Space ? O(1)
# Stabe ? No
# Inplace ? Yes

class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0
    
    def getParent(self,i):
        return (i-1)//2
    def getLeftChild(self,i):
        return 2*i+1
    def getRightChild(self, i):
        return 2*i+2

    def hasParent(self,i):
        return self.getParent(i)>=0
    def hasLeftChild(self,i):
        return self.getLeftChild(i)<self.size
    def hasRightChild(self,i):
        return self.getRightChild(i)<self.size
    
    def swap(self, i, j):
        self.heap[i],self.heap[j]= self.heap[j],self.heap[i]
    
    def insertKey(self,val):
        self.heap.append(val)
        self.size+=1
        self.heapify()

    def heapify(self):
        index = self.size - 1
        while(self.hasParent(index) and self.heap[self.getParent(index)]<self.heap[index]):
            self.swap(index, self.getParent(index))
            index = self.getParent(index)
    
    def deleteRoot(self):
        if self.size==0:
            return -1
        self.swap(0, self.size-1)
        self.size -= 1
        root = self.heap.pop()
        self.heapifyDown()
        return root
    
    def heapifyDown(self):
        i = 0 
        while(self.hasLeftChild(i)):
            maxChildInd = self.maxChildIndex(i)
            if maxChildInd==-1:
                break
            if self.heap[i]<self.heap[maxChildInd]:
                self.swap(i, maxChildInd)
                i = maxChildInd
            else:
                break

    def maxChildIndex(self, index):

        if self.hasLeftChild(index):
            leftChildIndex = self.getLeftChild(index)
            if self.hasRightChild(index):
                rightChildIndex = self.getRightChild(index)
                return leftChildIndex if self.heap[leftChildIndex]>=self.heap[rightChildIndex] else rightChildIndex
            return leftChildIndex
        return -1
    
    def printHeap(self):
        print(self.heap)


max_heap = MaxHeap()
arr = [45,99,63,27,29,57,42,35,12,24]

for i in arr:
    max_heap.insertKey(i)
    #max_heap.insertKey(-i)  ####for min heap

max_heap.insertKey(50)
max_heap.printHeap()
max_heap.deleteRoot()
max_heap.printHeap()
max_heap.deleteRoot()
max_heap.printHeap()
max_heap.deleteRoot()
max_heap.printHeap()
max_heap.deleteRoot()
max_heap.printHeap()
while(max_heap.size):
    print(max_heap.deleteRoot())
    #print(-1*max_heap.deleteRoot())   ###for min heap
