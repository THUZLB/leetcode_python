# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        head_now = head
        m = 0
        backup = head
        while head_now.next != None:
            head_now = head_now.next
            backup = backup.next if m == n else backup
            m = m + 1 if m < n else n

        if backup == head and m == n - 1:
            return head.next
        else:
            backup.next = backup.next.next
            return head


# best in Leetcode
# 意思相同，更简洁一点
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        lead = head
        for _ in range(n):
            lead = lead.next
        if not lead:
            return head.next
        follow = head
        while lead.next:
            lead = lead.next
            follow = follow.next
        follow.next = follow.next.next
        return head
