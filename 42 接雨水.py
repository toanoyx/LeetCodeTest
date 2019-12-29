# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入：[0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6

class Solution:
    def trap(self, height: List[int]) -> int:
        ans,h1,h2=0,0,0
        for i in range(len(height)):
            h1=max(h1,height[i])
            h2=max(h2,height[-i-1])
            ans=ans+h1+h2-height[i]
        return ans-len(height)*h1
