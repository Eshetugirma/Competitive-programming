class Solution:
    def maxLength(self, arr: List[str]) -> int:
#==> this is backtracking solution for this problem
        # stack = []
        # self.ans = 0
        # def backtracking(index,temp,arr):
        #     if len(temp) != len(Counter(temp)):
        #         return 
        #     self.ans = max(self.ans,len(temp))
        #     print(temp,index)
        #     for i in range(index,len(arr)):
        #         backtracking(i+1,temp+arr[i],arr)
        # backtracking(0,"",arr)
        # return self.ans

#==> this is iterative approach
        stack = [""]
        ans = 0
        for index in range(len(arr)):
            for i in range(len(stack)):
                temp =  stack[i] + arr[index]
                if len(temp) == len(Counter(temp)):
                    stack.append(temp)
                    ans = max(ans,len(temp))
        return ans



            

                

