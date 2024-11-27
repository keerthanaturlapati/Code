# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.


class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indexes=[]
        count=0
        for i in nums:
            if i==1:
                indexes.append(count)
            count=count+1
        print(indexes)
        j=0
        while(j<(len(indexes))):
            print j
            if(j==len(indexes)-1):
                return True
            elif((indexes[j+1]-indexes[j])<=k ):
                return False
            j=j+1
        return True
