# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 输入：[2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, len(nums)-1, 0
        while k < len(nums):
            if nums[k] == 0 and k > i:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            elif nums[k] == 2 and k < j:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k+=1
