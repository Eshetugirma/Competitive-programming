class Solution:
    def minimumSteps(self, s: str) -> int:

        count, left, right = 0, 0, len(s)-1

        while left < right:

            if s[right] == '1':
                right -= 1

            elif s[left] == '1':
                count += right - left
                left += 1
                right -= 1

            else:
                left += 1

        return count
        