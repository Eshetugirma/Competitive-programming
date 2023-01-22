class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        temp = []
        # ==> first i try to sort arr1 with respect to element in arr2
        for num_in_arr2 in arr2:
            for num_in_arr1 in arr1:
                if num_in_arr1 == num_in_arr2:
                    ans.append(num_in_arr1)
        # ==> now i'm recordind element that are not in arr2 in to temporary container temp
        for num in arr1:
            if num not in arr2:
                temp.append(num)
        # ==> then separetly sort element in temp
        temp.sort()
        return ans + temp   # ==>> finally return both ans and temp
        