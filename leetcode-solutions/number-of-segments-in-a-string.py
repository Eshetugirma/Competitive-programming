class Solution:
    def countSegments(self, s: str) -> int:
        # Initialize a variable to keep track of the count of segments.
        count = 0
        # Initialize a flag to check if we are inside a segment.
        inside_segment = False
        
        # Iterate through each character in the string.
        for char in s:
            # If the current character is not a space and we are not inside a segment, start a new segment.
            if char != ' ' and not inside_segment:
                count += 1
                inside_segment = True
            # If the current character is a space and we are inside a segment, mark the end of the segment.
            elif char == ' ' and inside_segment:
                inside_segment = False
        
        return count