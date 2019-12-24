# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 输入：123
# 输出：321

class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)[::-1].rstrip('-')
        if int(s)<2**31:
            if x>0:
                return int(s)
            else:
                return 0-int(s)
        return 0
