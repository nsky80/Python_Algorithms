arr = [3, 2, 6, 4, 9, 3]
heap_size = len(arr)

def max_heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)


if __name__ == '__main__':
    print(arr)
    max_heapify(arr, 1)
    print(arr)
