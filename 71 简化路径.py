# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
# 输入：/home/
# 输出：/home

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for i in path.split('/'):
            if i not in ['','.','..']:
                stack.append(i)
            elif i=='..' and stack:
                stack.pop()
        return "/"+"/".join(stack)
