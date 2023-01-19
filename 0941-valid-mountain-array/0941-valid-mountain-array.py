class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        checker = sorted(arr)
        checker2 = sorted(arr,reverse = True)
        if len(arr)<3 or arr == checker or arr == checker2: # check if sorted and length < 3
            return False
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            elif arr[i] > arr[i+1]:
                temp = i
                break
        for j in range(temp,len(arr)-1):
            if arr[j] <= arr[j+1]:
                return False
        return True