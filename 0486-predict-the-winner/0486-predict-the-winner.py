class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        start = 0
        end = len(nums)-1
        def pred(start,end,player1_turn):
            if start == end:
                if player1_turn:
                    return [nums[start],0]
                else:
                    return [0,nums[start]]
            
            if player1_turn:
                start_res = pred(start+1,end,False)
                start_res[0] += nums[start]
                end_res = pred(start,end-1,False)
                end_res[0] += nums[end]
                if start_res[0]>end_res[0]:
                    return start_res
                else:
                    return end_res
            else:
                start_res = pred(start+1,end,True)
                start_res[1] += nums[start]
                end_res = pred(start,end-1,True)
                end_res[1] += nums[end]
                if start_res[1]>end_res[1]:
                    return start_res
                else:
                    return end_res
        result = pred(start,end,True)
        if result[0] >= result[1]:
            return True
        else: 
            return False
        