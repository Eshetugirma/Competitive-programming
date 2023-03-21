class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occ = {}
        existance = set()

        for i in range(len(s)):
            last_occ[s[i]] = i

        for i in range(len(s)):

            while stack and stack[-1] >= s[i] and i <= last_occ[stack[-1]] and s[i] not in existance:
                existance.remove(stack.pop())
                
            if s[i] not in existance:
                stack.append(s[i])
                existance.add(s[i])
        return "".join(stack)