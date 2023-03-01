class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = []
        check = 0
        for i in range(len(s)):
            if s[i] == "(":
                check = 1
                stack.append("(")
            if s[i] == ")":
                if check == 1:
                    count += 2**(len(stack)-1)
                    check = 0
                stack.pop()
        return count
                
            