class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        result = len(nums)//2
        return nums[result]