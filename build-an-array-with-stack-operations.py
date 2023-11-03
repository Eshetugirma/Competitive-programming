class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        pointer = 0
        for curr in range(1,n+1):
            if pointer == len(target):
                break
            elif target[pointer] != curr:
                stack.append("Push")
                stack.append('Pop')
            else:
                stack.append('Push')
                pointer += 1
        return stack