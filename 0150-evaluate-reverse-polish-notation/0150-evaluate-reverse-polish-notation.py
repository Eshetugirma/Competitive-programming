class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "-":
                pop = stack.pop()
                stack.append(int(stack.pop()) - int(pop))
            elif tokens[i] == "+":
                pop = stack.pop()
                stack.append(int(stack.pop()) + int(pop))                
            elif tokens[i] == "*":
                pop = stack.pop()
                stack.append(int(stack.pop()) * int(pop))
            elif tokens[i] == "/":
                pop = stack.pop()
                stack.append(int(stack.pop()) / int(pop))
            else:
                stack.append(tokens[i])
        return int(stack[0])