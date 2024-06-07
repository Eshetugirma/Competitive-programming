class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        sorted_dict = sorted(count.keys())
        for key in sorted_dict:
            if count[key] > 0:
                start_count = count[key]
                for i in range(key,key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True