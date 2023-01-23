class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        target = len(arr)
        # ==>> loop up to all elements are sorted 
        while target != 0:
            i = arr.index(target)
            # ==>> if the largest number is get his place then reduce my target and continue
            if i + 1 == target:
                target -= 1
                continue
            # ==>> if index of target is zero then reverse elements lenght of target else up to position of target
            if i == 0 :
                k = target
            else:
                k = i + 1
            arr = arr[:k][::-1] + arr[k:]
            # ==>> append lenght of reversed elements
            ans.append(k)
        return ans