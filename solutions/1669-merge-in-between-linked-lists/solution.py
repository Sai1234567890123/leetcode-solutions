# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Find the node right before index `a` (index a - 1)
        # and the node right after index `b` (index b + 1).
        curr = list1
        node_before_a = None
        node_after_b = None
        
        # Traverse list1 up to index b + 1
        for idx in range(b + 1):
            if idx == a - 1:
                node_before_a = curr
            curr = curr.next
        
        # After loop, curr is at index b + 1
        node_after_b = curr

        # Step 2: Find the tail of list2
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        # Step 3: Splice list2 in place of the removed sublist
        node_before_a.next = list2
        tail2.next = node_after_b

        return list1
