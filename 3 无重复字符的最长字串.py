# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 输入：abcabcbb
# 输出：3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        res = []
        for x in s:
            if x not in l:
                l.append(x)
            else:
                res.append(len(l))
                i = l.index(x)
                l = l[i+1:]
                l.append(x)
        res.append(len(l))
        return max(res) if res else 0
