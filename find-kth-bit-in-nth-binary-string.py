class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        #==>>> this is to invert and reverse string came in to this function as parameter 
        def invert(ans): 
            ans = ans[::-1]
            temp = ""
            for i in ans:

                if int(i) == 1:
                    temp += "0"
                else:
                    temp += "1"
            return temp
        #==>>> this is function which form bit or binary string
        def reverse(num):

            if num == 1:
                return "0"
            bits = reverse(num-1)
            return bits + "1" + invert(bits)
        s = reverse(n)
        return s[k-1]