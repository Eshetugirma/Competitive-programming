class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        temp = []
        # ==> first i try to sort arr1 with respect to element in arr2
        for i in range(len(arr2)):
            for j in arr1:
                if arr2[i] == j:
                    ans.append(j)
        # ==> now i'm recordind element that are not in arr2 in temporary containor temp
        for num in arr1:
            if num not in arr2:
                temp.append(num)
        # ==> then separetly sort element in temp
        temp.sort()
        return ans + temp   # ==>> finally return both ans and temp
        