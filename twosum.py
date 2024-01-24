from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict =  {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in dict:
                return [dict[target - nums[i]],i]
            dict[nums[i]] = i
            

c = Solution()
print(c.twoSum([9,5,95,845,24,1,84,9,0],6))