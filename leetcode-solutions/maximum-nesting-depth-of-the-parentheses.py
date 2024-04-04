class Solution:
    def maxDepth(self, s: str) -> int:
        local_max, global_max = 0, 0
        for char in s:
            if char == "(":
                local_max += 1
            elif char == ")":
                local_max -= 1
            global_max = max(local_max,global_max)
        return global_max
        