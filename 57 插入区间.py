# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(reverse = True)
        for i in range(len(intervals)-1, 0, -1):
            if(intervals[i][0]<=intervals[i-1][1]) and (intervals[i][1]>=intervals[i-1][0]):
                intervals[i-1] = [min(intervals[i]+intervals[i-1]),max(intervals[i]+intervals[i-1])]
                intervals.pop(i)
        return sorted(intervals)
