class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i ,n in enumerate(nums):
            if n in hash and abs(hash[n] - i) <=k:
                return True
            hash[n] = i
        return False
