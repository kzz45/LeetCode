"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_sum = max_sum = nums[0]
        for i in range(1, n):
            cur_sum = max(nums[i], cur_sum+nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = nums[0]
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
        return max_sum


class Solution3(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tmp = max_sum = nums[0]
        for i in range(1, n):
            if tmp+nums[i] > nums[i]:
                max_sum = max(max_sum, tmp+nums[i])
                tmp = tmp+nums[i]
            else:
                max_sum = max(max_sum, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_sum
