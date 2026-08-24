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
        if not head: return None
        hashmap = {}
        curr = head

        #Creates nodes and adds it tot he hashmap
        while curr:
            new = Node(curr.val)
            hashmap[curr] = new
            curr = curr.next

        curr = head
        #Uses hashmap to assign next and random points
        while curr:
            new = hashmap[curr]
            new.random = hashmap[curr.random] if curr.random else None
            new.next = hashmap[curr.next] if curr.next else None
            curr = curr.next

        #Return new head
        return hashmap[head]