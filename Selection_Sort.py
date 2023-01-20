#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        i = int(input())
        #arr = [input()for _ in range(i-2)]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            #arr[i],min(arr[i:]) = min(arr[i:]),arr[i]
            temp = i
            for j in range(i,n):
                if arr[j]<arr[temp]:
                    temp = j
            if temp != i:
                arr[i],arr[temp] = arr[temp],arr[i]
            
            

