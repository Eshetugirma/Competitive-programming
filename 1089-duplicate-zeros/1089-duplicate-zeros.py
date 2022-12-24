class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left_pointer = 0
        right = len(arr)-1
        while  (left_pointer < right):
            if arr[left_pointer] == 0:
                arr.pop()
                arr.insert(left_pointer,0)
                left_pointer += 1
            left_pointer += 1