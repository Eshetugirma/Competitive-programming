class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if  arr[i] * 2 in arr[0:i] + arr[i+1:]  or arr[i] / 2 in arr[0:i]+ arr[i+1:]:
                return True
        return False
