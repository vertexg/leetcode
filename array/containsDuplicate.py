class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for i in nums:
          counter[i] += 1
          if counter[i] > 1:
            return True
        return False

# http://leetcode.com/problems/contains-duplicate/description/
