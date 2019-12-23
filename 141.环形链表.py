# 给定一个链表，判断链表中是否有环。
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是  -1，则在该链表中没有环。
# 输入1：head = [3,2,0,-4], pos = 1
# 输出1：true
# 输入2：head = [1,2], pos = 0
# 输出2：true
# 输入3：head = [1], pos = -1
# 输出3：false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        while head.next and head.val!=None:
            head.val=None
            head=head.next
        if not head.next:
            return False
        else:
            return True
