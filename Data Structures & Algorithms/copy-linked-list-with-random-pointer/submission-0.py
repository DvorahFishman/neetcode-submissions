"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dict_nodes ={}
        
        while curr:
            new_node = Node(curr.val)
            dict_nodes[curr] = new_node
            curr = curr.next

        for original_node, new_node in dict_nodes.items():
            new_node.next = dict_nodes.get(original_node.next)
            new_node.random = dict_nodes.get(original_node.random)

        return dict_nodes.get(head)