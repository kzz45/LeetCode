"""
给定一个链表, 返回链表开始入环的第一个节点, 如果链表无环, 则返回null
"""


class Solution(object):
    def detectCycle(self, head):
        slow = fast = head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            # 第一次相遇
            if fast == slow:
                break
        # 快的指针从头在跑
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        # 第二次相遇就是入环的节点
        return fast


"""
给定一个链表, 如果链表有环返回环的长度, 如果无环返回null
"""
