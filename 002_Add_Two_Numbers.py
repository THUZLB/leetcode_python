# -*- coding: utf-8 -*-
# author: THUZLB
# GitHub: https://github.com/THUZLB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeSum = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        node1 = l1.next
        node2 = l2.next
        node = ListNode(nodeSum)
        nodeIter = node
        while not (node1 is None and node2 is None and carry == 0):
            if node1 is None and node2 is not None:
                nodeSum = (node2.val + carry) % 10
                carry = (node2.val + carry) // 10
                nodeIter.next = ListNode(nodeSum)
                nodeIter = nodeIter.next
                node2 = node2.next
            elif node2 is None and node1 is not None:
                nodeSum = (node1.val + carry) % 10
                carry = (node1.val + carry) // 10
                nodeIter.next = ListNode(nodeSum)
                nodeIter = nodeIter.next
                node1 = node1.next
            elif node1 is not None and node2 is not None:
                nodeSum = (node1.val + node2.val + carry) % 10
                carry = (node1.val + node2.val + carry) // 10
                nodeIter.next = ListNode(nodeSum)
                nodeIter = nodeIter.next
                node1 = node1.next
                node2 = node2.next
            else:
                nodeSum = carry
                carry = 0
                nodeIter.next = ListNode(nodeSum)
                nodeIter = nodeIter.next
        
        return node
