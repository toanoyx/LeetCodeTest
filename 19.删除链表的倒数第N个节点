# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 输入：1->2->3->4->5, 和 n = 2
# 输出：1->2->3->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=slow=head               # 快慢双指针
        for i in range(n):           # 让快指针先走n步
            fast=fast.next
        if fast == None:             # 若走了n步后为空，则要删除的是head节点
            return head.next
        while fast.next:             # 快慢指针同时向前走，步距为n，快指针走到头时，慢指针的下一个即是要删除的节点
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next     # 删除该节点
        return head  
