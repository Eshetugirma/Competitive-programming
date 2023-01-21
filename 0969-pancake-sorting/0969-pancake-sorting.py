class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        swaps = []
        target = len(arr)
        while target != 0:
            i = arr.index(target)
            if i + 1 == target:
                target -= 1
                continue

            k = target if i == 0 else i + 1
            arr = arr[:k][::-1] + arr[k:]
            swaps.append(k)

        return swaps