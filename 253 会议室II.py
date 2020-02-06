# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

# 输入：[[0, 30],[5, 10],[15, 20]]
# 输出：2

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        occupied, res = [], 0
        intervals.sort(key = lambda x:x[0])
        for i in intervals:
            start, end = i
            occupied = [t for t in occupied if t > start]
            occupied.append(end)
            res = max(res, len(occupied))
        return res
