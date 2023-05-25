class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                tens += 1
                fives -= 1
            else:
                if fives >= 3 and not tens:
                    fives -= 3
                else:
                    tens -= 1
                    fives -= 1
            if tens < 0 or fives < 0:
                
                return False
        return True