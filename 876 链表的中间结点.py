# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。
# 输入：[1,2,3,4,5]
# 输出：[3,4,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast=slow=head                          # 快慢指针
        while fast.next and fast.next.next:     # 当快指针一次两步，慢指针一次一步，快指针走到空时，慢指针为中间结点
            fast=fast.next.next
            slow=slow.next
        if fast.next==None:                     # 一个中间结点的情况
            return slow
        else:                                   # 两个中间结点的情况
            return slow.next
