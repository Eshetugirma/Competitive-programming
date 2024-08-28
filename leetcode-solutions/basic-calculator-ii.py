class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        check = ['/','-','+','*']
        st = []
        for c in s:
            if c != ' ': 
                if st and c not in check and st[-1] not in check:
                    curr = st.pop() + c
                    st.append(curr)
                else:
                    st.append(c)
            
        for c in st:
            if stack and stack[-1] == '*':
                stack.pop()
                curr = int(stack.pop())*int(c)
                stack.append(str(curr))
            elif stack and stack[-1] == '/':
                stack.pop()
                a = stack.pop()
                curr = int(a)//int(c)
                stack.append(str(curr))
            else:
                stack.append(c)
        ans = 0
        sign = 1
        for c in stack:
            if c == '-':
                sign = 0
            elif c == '+':
                sign = 1
            else:
                if sign:
                    ans += int(c)
                else:
                    ans -= int(c)
        return ans

                

