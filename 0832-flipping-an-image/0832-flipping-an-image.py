class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # ===>>> flip the row by reversing it
        for row in range(len(image)):
            image[row].reverse()
        # ===>>> invert the value of every binary value in matrix
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
        return image