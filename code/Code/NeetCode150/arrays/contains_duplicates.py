# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        for i in nums:
            if i in dict1.keys():
                return True
            else:
                dict1.update({i:1})
        return False