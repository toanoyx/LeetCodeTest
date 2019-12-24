# 请判断一个链表是否为回文链表。
# 输入：1->2
# 输出：false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast=slow=head
        while fast:                                             # 快慢指针法，让慢指针走到中点
            slow=slow.next
            fast=fast.next.next if fast.next else fast.next
        p,rev = slow,None
        while p:
            rev,rev.next,p = p,rev,p.next                       # 将中点之后的链表反转
        while rev:                                              # 重新以head开始比较反转之后的链表
            if rev.val!=head.val:
                return False
            rev=rev.next
            head=head.next
        return True
