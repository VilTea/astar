import numpy as np
import npfunc as npf

from searchfunc import a_star
from listnode import ListNode


if __name__ == '__main__':
    start = np.array([[8, 3, 2], [0, 1, 4], [7, 6, 5]])
    # start = np.array([[1, 2, 3], [8, 4, 5], [7, 6, 0]])
    end = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    Ahead = ListNode(val=start, cost=npf.get_distance(start, end))
    Atarget = ListNode(val=end)
    Aroad = a_star(head=Ahead, target=Atarget, bulit_func=npf.built_next, dist_func=npf.get_distance
                   , find_func=npf.find_in_list, judge_func=npf.judge)
    for i, elem in enumerate(Aroad):
        print('----- status', i, '-----')
        print(elem.get_val())
        print('f:', elem.get_f())
    pass


