# 给定两个数组，编写一个函数来计算它们的交集。

# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
