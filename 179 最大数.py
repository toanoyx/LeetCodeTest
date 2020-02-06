# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

# 输入：[3,30,34,5,9]
# 输出：9534330

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s = ''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
        for i in nums:
            s += str(i)
        return str(int(s))
