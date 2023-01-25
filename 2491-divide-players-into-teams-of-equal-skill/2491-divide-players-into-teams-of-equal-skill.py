class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # ==>>>> diclare the target which it will be if the proccess is true
        target = sum(skill)*2//len(skill)
        skill.sort()
        right = len(skill)-1
        left = 0
        product_of_pairs = []
        # ===>>> check if sum of pair is out of target we are finding
        while right > left:
            if skill[right]+skill[left] == target:
                product_of_pairs.append(skill[right]*skill[left])
                right -= 1
                left += 1
            else:
                return -1
        # ==>> return sum of all product
        return sum(product_of_pairs)