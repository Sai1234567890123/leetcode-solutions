# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes the given node from a singly-linked list in-place.
        Modifies node directly; does not return anything.
        """
        # Since we cannot modify the previous node's `next` pointer,
        # we copy the value of the next node into the current node.
        node.val = node.next.val
        
        # Bypass the next node, effectively deleting it from the list.
        node.next = node.next.next
