class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range (len(nums)):
        for b in range (i+1, len(nums)):
          if target == nums[i] + nums[b]:
            return [i,b]


# https://leetcode.com/problems/two-sum/
