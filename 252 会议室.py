# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加这里面的全部会议。

# 输入：[[0,30],[5,10],[15,20]]
# 输出：false

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        istart = sorted(intervals, key = lambda x:x[0])
        for i in range(1, len(istart)):
            if istart[i][0] < istart[i - 1][1]:
                return False
        return True
