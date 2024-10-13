class Solution:
    def decodeString(self, s: str) -> str:
        
        integers = ['1','2','3','4','5','6','7','8','9','0']
        stack = []

        for char in s:

            if char == ']':

                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp

                stack.pop()

                num = ''
                while stack and stack[-1] in integers:
                    num = stack.pop() + num
                
                try:
                    char = temp*(int(num))

                except:
                    char = temp
            
            stack.append(char)

        return ''.join(stack)