class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")" :"(" ,
            "]" : "[" ,
            "}" : "{"
        }
        stack = []
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if stack: 
                    if dic[s[i]] == stack[-1]:
                        stack.pop()
                    else:
                        break
                else:
                    stack.append(s[i])
        return not len(stack)
                    
            