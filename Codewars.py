"""
This file here just for tmp tests
All tasks in 'Codewars.ipynb'
"""


class Solution(object):
    @staticmethod
    def middle_node(head):
        middle_node_index = int(round(len(head) / 2, 0))
        return head[middle_node_index:]


head = [1, 2, 3, 4, 5, 6]
print(Solution.middle_node(head))
