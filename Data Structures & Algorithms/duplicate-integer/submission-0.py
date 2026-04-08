class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 1
        while len(nums) > i:
            if nums[i-1] == nums[i]:
                return True
            i+=1
        return False
        