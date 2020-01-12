# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 输入：babad

# 输出：bab

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s
        
        def helper(i,j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if self.max_len < j - i - 1:
                self.max_len = j - i - 1
                self.start = i + 1
         
        for k in range(n):
             helper(k, k)
             helper(k, k+1)
        return s[self.start:self.start+self.max_len]
