class Solution:
    def decodeString(self, s: str) -> str:
        dig = ['1','2','3','4','5','6','7','8','9','0']
        stack = []
        #==>>> edge case if no brackets
        if "[" not in s and s[0] in dig:
            return ""
        elif "[" not in s and s[0] not in dig:
            return s
        #==>> using stack we can solve this problem
        for i in range(len(s)):
            #==>> append any element until u see "]"
            if s[i] != "]":
                stack.append(s[i])
            #==>>> if see "]" then pop str after opening brace
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                num = ""
                #==>> if see digit collect on num 
                while stack and stack[-1] in dig:
                    num = stack.pop() + num
                #==>> now multiply substr by num and append back to stack 
                stack.append(int(num) * substr)
        return "".join(stack)
                    