class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if not i%3 and not i%5:
                ans.append("FizzBuzz")
            elif not i%3:
                ans.append("Fizz")
            elif not i%5:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans