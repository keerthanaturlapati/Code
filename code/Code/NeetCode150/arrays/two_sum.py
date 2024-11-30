# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1={}
        count=0
        for i in nums:
            diff=target-i
            if(diff in dict_1.keys()):
                return([dict_1[diff],count])
            else:
                dict_1.update({i:count})
            count+=1