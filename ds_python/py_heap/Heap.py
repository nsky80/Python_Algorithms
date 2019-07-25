"""
Applications of Heaps:
1) Heap Sort: Heap Sort uses Binary Heap to sort an array in O(nLogn) time.

2) Priority Queue: Priority queues can be efficiently implemented using Binary Heap because it supports insert(),
delete() and extractmax(), decreaseKey() operations in O(logn) time.
Binomial Heap and Fibonacci Heap are variations of Binary Heap. These variations perform union also efficiently.

3) Graph Algorithms: The priority queues are especially used in Graph Algorithms like Dijkstra’s Shortest
Path and Prim’s Minimum Spanning Tree.

4) Many problems can be efficiently solved using Heaps. See following for example.
a) K’th Largest Element in an array.
b) Sort an almost sorted array/
c) Merge K Sorted Arrays.

Operations on Min Heap:
1) getMini(): It returns the root element of Min Heap. Time Complexity of this operation is O(1).

2) extractMin(): Removes the minimum element from MinHeap. Time Complexity of this Operation is O(Logn) as this
operation needs to maintain the heap property (by calling heapify()) after removing root.

3) decreaseKey(): Decreases value of key. The time complexity of this operation is O(Logn).
If the decrease key value of a node is greater than the parent of the node, then we don’t need to do anything.
Otherwise, we need to traverse up to fix the violated heap property.

4) insert(): Inserting a new key takes O(Logn) time. We add a new key at the end of the tree. IF new key is greater than
its parent, then we don’t need to do anything. Otherwise, we need to traverse up to fix the violated heap property.

5) delete(): Deleting a key also takes O(Logn) time. We replace the key to be deleted with minum infinite by calling
decreaseKey(). After decreaseKey(), the minus infinite value must reach root, so we call extractMin() to remove the key.

Below is the implementation of basic heap operations
"""

heap_size = 0


def Max_Heapify(arr, i):
    global heap_size
    left = 2 * i + 1
    r = 2 * i + 2
    if left < heap_size and arr[i] < arr[left]:
        largest = left
    else:
        largest = i
    if r < heap_size and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        Max_Heapify(arr, largest)


def Min_heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2


def Build_Max_Heap(arr):
    global heap_size
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        # print(arr)
        Max_Heapify(arr, i)
    # print(arr)


# arr = [8, 7, 6, 3, 2, 4, 5]   [6, 4, 5, 3, 2, 0, 1]
arr = [1, 4, 3, 7, 8, 9, 10]
Build_Max_Heap(arr)
print(arr)
