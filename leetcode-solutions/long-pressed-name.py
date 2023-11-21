class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] : return False
        l = 0
        for r in range(len(typed)):

            if l < len(name) and typed[r] == name[l]:
                l += 1
            elif typed[r] != typed[r-1]:
                return False

        if l < len(name): return False
        
        return True