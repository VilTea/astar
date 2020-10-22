from typing import List


class ListNode:
    def __init__(self, val: any, depth: int = 0, cost: int = 0, parent=None, next_n=None, cousin=None):
        """
        树节点的二叉树表示
        :type val: any
        :type parent: ListNode
        :type next_n: ListNode
        :type cousin: ListNode
        :param val: 节点值
        :param depth: 节点深度
        :param cost: 节点代价
        :param parent: 父节点
        :param next_n: 子节点
        :param cousin: 兄弟节点
        """
        self._val = val
        self._cost = cost
        self._parent = parent
        self._depth = depth
        self._next = next_n
        self._cousin = cousin

    def get_cost(self) -> int:
        return self._cost

    def get_depth(self) -> int:
        return self._depth

    def get_f(self) -> int:
        return self._cost + self._depth

    def get_val(self):
        return self._val

    def get_parent(self) -> __init__:
        return self._parent

    def get_next(self) -> __init__:
        return self._next

    def get_cousin(self) -> __init__:
        return self._cousin

    def set_next(self, next_n):
        self._next = next_n

    def set_cost(self, cost):
        self._cost = cost

    def set_depth(self, depth):
        self._depth = depth

    def set_cousin(self, cousin):
        self._cousin = cousin

    def get_road(self) -> List[__init__]:
        road = list()
        now = self
        while now.get_parent() is not None:
            road.append(now)
            now = now.get_parent()
        road.append(now)
        road.reverse()
        return road
