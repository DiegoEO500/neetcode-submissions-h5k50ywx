class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)): 
            for p in range(len(nums)): 
                check = nums[i] + nums[p]
                if check == target:
                    if i < p:
                        result.append(i)
                        result.append(p)
                        return result