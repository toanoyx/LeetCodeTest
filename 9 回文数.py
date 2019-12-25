# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 输入：121
# 输出：true

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1=str(x)[::-1]
        s2=str(x)
        if s1==s2:
            return True
        else:
            return False
