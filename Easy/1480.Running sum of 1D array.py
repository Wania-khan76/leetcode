class Solution(object):
    def runningSum(self, nums):
        a=[nums[0]]
        for i in range(1,len(nums)):
            a.append(a[-1]+nums[i])
        return a


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        count = 1
        while count < len(nums):
            nums[count] += nums[count - 1]
            count += 1
        return(nums)
