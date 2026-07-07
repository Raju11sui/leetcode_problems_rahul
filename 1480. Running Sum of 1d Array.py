from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """Return running sum of the input list in-place (also returns the list)."""
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
        