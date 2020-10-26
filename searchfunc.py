from typing import Optional, List
from listnode import ListNode


def a_star(head: ListNode, target: ListNode
           , bulit_func, dist_func, find_func, judge_func=None) -> Optional[List[ListNode]]:
    """
    A*算法
    :param head: 初始状态节点
    :param target: 目标状态节点
    :param bulit_func: 生成后继节点函数
    :param dist_func: 评估函数h(x)
    :param find_func: 寻址函数
    :param judge_func: 判断有解无解函数
    :return: 路径节点列表
    """
    if judge_func is not None and judge_func(head.get_val(), target.get_val()) is not True:
        print("无解")
        exit(1)
    ans = None
    opened, closed = list(), list()
    if head is not None:
        opened.append(head)
    while opened:
        now = opened.pop()
        # now.get_parent().set_cost()
        closed.append(now)
        if (now.get_val() == target.get_val()).all():
            ans = now.get_road()
            break
        now = bulit_func(now, cost_func=lambda x: dist_func(x.get_val(), target.get_val()),
                         # depth_func=lambda x: dist_func(head.get_val(), x.get_val()))
                         depth_func=lambda x: now.get_depth() + 1)
        next_node = now.get_next()
        while next_node is not None:
            m = find_func(next_node, closed)
            n = find_func(next_node, opened)
            if m is not None and next_node.get_f() < closed[m].get_f():
                if n is None:
                    opened.append(next_node)
                else:
                    opened[n] = next_node
                closed[m] = next_node
            if n is not None and next_node.get_f() < opened[n].get_f():
                opened[n] = next_node
            if m is None and n is None:
                opened.append(next_node)
            next_node = next_node.get_cousin()
        opened.sort(key=lambda x: x.get_f(), reverse=True)
    return ans
