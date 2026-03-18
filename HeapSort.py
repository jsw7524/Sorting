import heapq
def heapSort(arr):
    n = len(arr)
    result=[]
    # Build a maxheap.
    heapq.heapify(arr)

    # One by one extract elements from heap
    for i in range(n):
        val=heapq.heappop(arr)
        result.append(val)
    return result