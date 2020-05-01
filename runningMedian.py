class minHeap:
    def __init__(self,heap_list = []):
        self.heap = heap_list
        self.length = len(self.heap)
    def get_parent(self,i):
         return int((i-1)/2)
    def get_left_child(self,i):
        return 2*i + 1
    def get_right_child(self,i):
        return 2*i + 2
    def has_parent(self,i):
        return int((i-1)/2) >= 0
    def has_left_child(self,i):
        return 2*i + 1 < len(self.heap)
    def has_right_child(self,i):
        return 2*i + 2 < len(self.heap)
    def swap(self,i,j):
        (self.heap[i],self.heap[j]) = (self.heap[j],self.heap[i])
    def get_min_child(self,i):
        if self.has_left_child(i):
            left_child = self.get_left_child(i)
            if self.has_right_child(i):
                right_child = self.get_right_child(i)
                if self.heap[left_child] < self.heap[right_child]:
                    return left_child
                else:
                    return right_child
            else:
                return left_child
    def insert(self,x):
        self.length += 1
        self.heap.append(x)
        i = len(self.heap) -1
        while self.has_parent(i):
            parent_index = self.get_parent(i)
            if self.heap[i] < self.heap[parent_index]:
                self.swap(parent_index,i)
                i = parent_index
            else:
                break
    def delete(self,i):
        self.length -= 1
        i = 0
        self.swap(i,len(self.heap)-1)
        deleted =self.heap.pop()
        while self.has_left_child(i):
            min_child = self.get_min_child(i)
            if self.heap[min_child] < self.heap[i]:
                self.swap(i,min_child)
                i = min_child
            else:
                break
        return deleted
class maxHeap:
    def __init__(self,heap_list = []):
        self.heap = heap_list
        self.length = len(self.heap)
    def get_parent(self,i):
         return int((i-1)/2)
    def get_left_child(self,i):
        return 2*i + 1
    def get_right_child(self,i):
        return 2*i + 2
    def has_parent(self,i):
        return int((i-1)/2) >= 0
    def has_left_child(self,i):
        return 2*i + 1 < len(self.heap)
    def has_right_child(self,i):
        return 2*i + 2 < len(self.heap)
    def swap(self,i,j):
        (self.heap[i],self.heap[j]) = (self.heap[j],self.heap[i])
    def get_max_child(self,i):
        if self.has_left_child(i):
            left_child = self.get_left_child(i)
            if self.has_right_child(i):
                right_child = self.get_right_child(i)
                if self.heap[left_child] > self.heap[right_child]:
                    return left_child
                else:
                    return right_child
            else:
                return left_child
    def insert(self,x):
        self.length += 1
        self.heap.append(x)
        i = len(self.heap) -1
        while self.has_parent(i):
            parent_index = self.get_parent(i)
            if self.heap[i] > self.heap[parent_index]:
                self.swap(parent_index,i)
                i = parent_index
            else:
                break
    def delete(self,i):
        self.length -= 1
        self.swap(i,len(self.heap)-1)
        deleted =self.heap.pop()
        while self.has_left_child(i):
            max_child = self.get_max_child(i)
            if self.heap[max_child] > self.heap[i]:
                self.swap(i,max_child)
                i = max_child
            else:
                break
        return deleted
n = int(input())
myMaxHeap = maxHeap()
myMinHeap = minHeap()
n1 = int(input())
print(n1)
myMaxHeap.insert(n1)
for _ in range(n-1):
    element = int(input())
    if element < myMaxHeap.heap[0]:
        myMaxHeap.insert(element)
    else:
        myMinHeap.insert(element)
    if (myMaxHeap.length - myMinHeap.length) > 1:
        root_deleted = myMaxHeap.delete(0)
        myMinHeap.insert(root_deleted)
    elif myMinHeap.length - myMaxHeap.length > 1:
        root_deleted = myMinHeap.delete(0)
        myMaxHeap.insert(root_deleted)
    if myMaxHeap.length == myMinHeap.length:
        median = (myMinHeap.heap[0] + myMaxHeap.heap[0])/2
        print(median)
    elif myMaxHeap.length > myMinHeap.length:
        print(myMaxHeap.heap[0])
    else:
        print(myMinHeap.heap[0])
