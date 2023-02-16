class Solution:
    def compress(self, chars: List[str]) -> int:
        placeholder = 0 
        mover = 0
        seeker = 0
        count = 0
        while seeker < len(chars):
            #===>>> count the number of consecutively repeated characters
            while seeker <len(chars) and chars[seeker] == chars[mover]:
                seeker +=1
                count +=1
            #==>>> if no repeated char store only character
            if count == 1:
                chars[placeholder] = chars[mover]
                placeholder += 1
                count = 0
            #==>>> if count of repeated char is less than ten store with count
            elif count>1 and count < 10:
                chars[placeholder] = chars[mover]
                placeholder +=1
                chars[placeholder] = str(count)
                placeholder +=1
                count = 0
            #===>>> if count is greater than ten store counted num separatly
            else:
                chars[placeholder] = chars[mover]
                placeholder +=1
                counted = str(count)
                for i in counted:
                    chars[placeholder] = i
                    placeholder +=1
                count = 0
            mover = seeker
        return placeholder

                            
        