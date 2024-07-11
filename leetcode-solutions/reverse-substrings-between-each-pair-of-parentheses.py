class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = collections.deque([])
        temp = ""
        for i in s:
            if i == "(":
                stack += temp,
                temp = ""
            elif i == ")":
                temp = stack.pop() + temp[::-1]
            else:
                temp += i
        return temp