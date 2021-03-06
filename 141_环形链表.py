"""
给定一个链表, 判断链表中是否有环
"""


# 定义单链表
class ListNode(object):
    def __init__(self, x):
        self.x = x
        self.next = None


# 哈希表

class Solution1(object):
    def hasCycle(self, head):
        nodeScan = set()
        point = head
        while point:
            if point in nodeScan:
                return True
            nodeScan.add(point)
            point = point.next
        return False


# 快慢指针


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class Solution3(object):
    def detectCycle(self, head):
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return None
