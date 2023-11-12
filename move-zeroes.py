class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_digit = 0
        for nonzero_digit in range(len(arr)):
            if arr[nonzero_digit]:
                arr[zero_digit],arr[nonzero_digit] = arr[nonzero_digit],arr[zero_digit]
                zero_digit += 1
        return arr