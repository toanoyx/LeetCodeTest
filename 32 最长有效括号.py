# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 输入：)()())
# 输出：4

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res
