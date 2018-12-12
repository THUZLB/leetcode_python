# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        p = head
        q = head.next
        new_head = q if q else p
        if q:
            tmp = q.next
            q.next = p
            p.next = tmp
            p_old = p
            p = tmp
            q = tmp.next if tmp else None
        while q:
            p_old.next = q
            tmp = q.next
            q.next = p
            p.next = tmp
            p_old = p
            p = tmp
            q = tmp.next if tmp else None

        return new_head
