#User function Template for python3
import heapq
from heapq import heappush,heappop 
class Solution:
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        heap = []
        for val in arr:
            heappush(heap,val)
        for i in range(n):
            arr[i] = heappop(heap)
        