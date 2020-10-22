import numpy as np
from listnode import ListNode
from typing import Optional, Tuple


def built_next(node: ListNode, cost_func, depth_func) -> ListNode:
    """
    生成后继节点
    """
    head: ListNode = node
    pre: ListNode = node
    i: np.array = node.get_val()
    row, col = find_elem(i, 0)
    for dirt in range(4):
        if is_wall(i, dirt, row, col) is not True:
            now = ListNode(parent=head, val=__move_array(i, dirt, row, col))
            cost = cost_func(now)
            depth = depth_func(now)
            now.set_cost(cost)
            now.set_depth(depth)
            if pre is head:
                pre.set_next(now)
            else:
                pre.set_cousin(now)
            pre = now
    return head


def is_wall(node: np.array, dirt: int, row: int, col: int) -> bool:
    """
    :param node:
    :param dirt:
    :param row:
    :param col:
    :return:
    """
    ans = True
    if dirt == 0:  # 北 N
        ans = (row - 1 < 0)
    elif dirt == 1:  # 南 S
        ans = (row + 1 >= node.shape[0])
    elif dirt == 2:  # 西 W
        ans = (col - 1 < 0)
    elif dirt == 3:  # 东 E
        ans = (col + 1 >= node.shape[1])
    return ans


def __move_array(val: np.array, dirt: int, row: int, col: int) -> np.array:
    node = val.copy()
    if dirt == 0:  # 北 N
        node[row][col], node[row - 1][col] = node[row - 1][col], node[row][col]
    elif dirt == 1:  # 南 S
        node[row][col], node[row + 1][col] = node[row + 1][col], node[row][col]
    elif dirt == 2:  # 西 W
        node[row][col], node[row][col - 1] = node[row][col - 1], node[row][col]
    elif dirt == 3:  # 东 E
        node[row][col], node[row][col + 1] = node[row][col + 1], node[row][col]
    return node


def find_in_list(node: ListNode, lt: list) -> Optional[int]:
    for n, elem in enumerate(lt):
        if (node.get_val() == elem.get_val()).all():
            return n
    return None


def find_elem(node: np.array, target: any) -> Optional[Tuple[int, int]]:
    """
    搜索目标元素
    :param node: 被搜索数组
    :param target: 搜索目标，请勿传入列表、元组、字典等复合数据类型
    :return: 被搜索目标在数组中的坐标
    """
    for row, list_elem in enumerate(node):
        for col, elem in enumerate(list_elem):
            if elem == target:
                return row, col
    return None


def get_distance(node1: np.array, node2: np.array) -> int:
    """
    获取距离
    """
    ans: int = 0
    for row, list_elem in enumerate(node1):
        for col, elem in enumerate(list_elem):
            if node2[row][col] != elem:
                ans += 1
    return ans


def __N(nums: np.array) -> int:
    nums = nums.copy().reshape(nums.shape[0] * nums.shape[1])
    N = np.sum([np.sum(nums[: idx] > val) for idx, val in enumerate(nums)])
    return N


def judge(start: np.array, end: np.array) -> bool:
    N1 = __N(start)
    N2 = __N(end)
    extra = 0 if start.shape[1] % 2 != 0 else abs(find_elem(start, 0)[1] - find_elem(end, 0)[1])
    if (N1 + extra) % 2 == N2 % 2:
        return True
    else:
        return False
