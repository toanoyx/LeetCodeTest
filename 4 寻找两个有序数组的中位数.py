# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。你可以假设 nums1 和 nums2 不会同时为空。

# 输入：nums1 = [1, 2]  nums2 = [3, 4]
# 输出：2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1 + nums2)
        mid = len(l) //2
        if len(l) % 2 == 0:
            return (l[mid] + l[mid - 1]) / 2
        else:
            return l[mid]
