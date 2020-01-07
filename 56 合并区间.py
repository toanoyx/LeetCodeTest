# 给出一个区间的集合，请合并所有重叠的区间。

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse = True)
        for i in range(len(intervals)-1, 0, -1):
            if(intervals[i][0]<=intervals[i-1][1]) and (intervals[i][1]>=intervals[i-1][0]):
                intervals[i-1] = [min(intervals[i]+intervals[i-1]),max(intervals[i]+intervals[i-1])]
                intervals.pop(i)
        return sorted(intervals)
