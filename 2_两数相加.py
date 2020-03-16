"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = cur = ListNode(0)
        first = True
        carry = 0
        while (l1 or l2 or carry != 0):
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            sums = val1 + val2 + carry
            if sums >= 10:
                carry = 1
                sums = sums % 10
            else:
                carry = 0
            node = ListNode(sums)
            if first:
                head = cur = node
                first = False
            else:
                cur.next = node
                cur = cur.next
        return head
