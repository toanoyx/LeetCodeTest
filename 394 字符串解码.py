# 给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 输入：3[a]2[bc]
# 输出：aaabcbc

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curStr = ""
        curNum = 0
        for a in s:
            if a.isdigit():
                curNum = curNum * 10 + int(a)
            elif a == '[':
                stack.append(curNum)
                stack.append(curStr)
                curStr = ""
                curNum = 0
            elif a == ']':
                curStr = stack.pop() + stack.pop() * curStr
            else:
                curStr += a
        return curStr
