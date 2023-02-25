class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [path[0]]
        pointer = 1        
        while pointer < len(path):

            if pointer+3 <= len(path) and path[pointer:pointer+3] == "../":
                if stack[-1] != "/":
                    stack.pop()
                pointer += 3
            elif pointer+2 < len(path) and path[pointer:pointer+2] == "./":
                pointer += 2
            elif pointer+1 < len(path) and path[pointer:pointer+1] == "/":
                pointer += 1
            elif pointer+2 <= len(path) and path[pointer:pointer+2] == "//":
                pointer += 2                
            else:
                st = ""
                while pointer < len(path) and path[pointer] != "/":
                    st += path[pointer]
                    pointer += 1
                if len(stack)>1 and st == "..":
                    stack.pop()
                elif st != "." and st != "..":
                    stack.append(st+"/")
                    pointer += 1
        ans = "".join(stack)
        while len(ans)>1 and ans[-1] == "/":
            ans = ans[:len(ans)-1]
        return ans
    
        

                
            