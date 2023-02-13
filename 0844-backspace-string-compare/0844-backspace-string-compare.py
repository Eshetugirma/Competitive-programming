class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        # ==>>> filter elements in list s
        for i in range(len(s)):
            if s[i] == "#":
                if ans1:
                    ans1.pop()
            else:
                ans1.append(s[i])
        # ==>> filter elements in list t
        for i in range(len(t)):
            if t[i] == "#":
                if ans2:
                    ans2.pop()
            else:
                ans2.append(t[i])
        #===>>> return their equivalence
        return ans1 == ans2