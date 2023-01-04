class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for index in range(len(command)):
            if command[index] == "(":
                if command[index+1] == ")":
                    ans.append("o")
            elif command[index] == ")":
                pass
            else:
                ans.append(command[index])
        return "".join(ans)