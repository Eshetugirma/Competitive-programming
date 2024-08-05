class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        for s in arr:
            if counter[s] == 1:
                k -= 1
                if not k:
                    return s
        return ""
            