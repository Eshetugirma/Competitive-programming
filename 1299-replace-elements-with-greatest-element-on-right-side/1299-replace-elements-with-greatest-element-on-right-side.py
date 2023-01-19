class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # >>> this is brute force solution and it is time limit exit
        '''
        # => first iterate all and then replace arr[i] with the maximum number 
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:]) 
            # replace arr[i] with the maximum number to the right 
        arr[-1] = -1   
        # update the last number with -1
        return arr
        '''
        # ==>>> this one is the working solution and best one at this time for me 
        arr.reverse()
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i+1] = arr[i]
        arr.pop()
        arr.reverse()
        arr.append(-1)
        return arr