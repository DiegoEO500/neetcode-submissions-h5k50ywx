class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i - 1] == nums[i]:
                if len(nums) > 1:
                    return True
        return False
        