class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = operations.count('--X') + operations.count('X--')
        return len(operations)-count*2