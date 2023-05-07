class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not (nums1 and nums2):
            return []
        heap = []
        visited = set()
        ans = []
        heappush(heap,(nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        while len(ans) < k and heap:
            temp = heappop(heap)
            ans.append([nums1[temp[1]],nums2[temp[2]]])
            if temp[1]+1 < len(nums1) and (temp[1]+1,temp[2]) not in visited:
                heappush(heap,(nums1[temp[1]+1]+nums2[temp[2]],temp[1]+1,temp[2]))
                visited.add((temp[1]+1,temp[2]))

            if temp[2]+1 < len(nums2) and (temp[1],temp[2]+1) not in visited:
                heappush(heap,(nums1[temp[1]]+nums2[temp[2]+1],temp[1],temp[2]+1))
                visited.add((temp[1],temp[2]+1))
        return ans