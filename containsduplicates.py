from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range (0,n-1):
            if nums[i] == nums[i+1]:
                return True
        return False 
    def containsDuplicateBetter(self, nums: List[int]) -> bool: #took up more memory lol, but like 40ms faster
        dict = {}
        for i in nums:
            dict[i] = dict.get(i,0) + 1
            if dict[i] == 2:
                return True
        return False
        
        
c = Solution()
print(c.containsDuplicateBetter([1,1,1,3,3,4,3,2,4,2]))