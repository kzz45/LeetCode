"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

# 暴力模式，两层循环相加等于目标


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return i, j

# 哈希表模式


class Solution2(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i, a in enumerate(nums):
            if target - a in hash_map:
                return hash_map[target-a], i
            else:
                hash_map[a] = i
