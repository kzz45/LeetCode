# LeetCode

数据结构最基础是数组和链表，从存储上而言，数组是连续的，链表是非连续的

操作数据无非增删改查，线性操作就是for循环，非线性操作就是递归迭代

定义一个最基础的链表的结点，一个结点分为数据部分和指针部分

```python
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
```

链表有单链表，双链表，循环链表。。。
