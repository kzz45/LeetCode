"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。


示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dump = ListNode(0)
        pre = dump
        while True:
            stack = []
            count = k
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp=tmp.next
                count -=1
            if count:
                pre.next=head
                break
            while stack:
                pre.next=stack.pop()
                pre=pre.next
            pre.next=tmp
            head =tmp
        return dump.next
