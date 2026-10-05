import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle edge cases:
        # If the list is empty or has only one node, there are no pairs of adjacent nodes.
        # In such cases, no insertions are needed, so return the head as is.
        if not head or not head.next:
            return head

        current = head
        # Iterate through the linked list. The loop continues as long as 'current'
        # is a valid node and it has a 'next' node, ensuring we always have a pair
        # (current, current.next) to process.
        while current and current.next:
            # Store the original next node temporarily. This is the second node
            # of the current pair (val1, val2).
            original_next = current.next

            # Get the values of the current node and its immediate successor.
            val1 = current.val
            val2 = original_next.val

            # Calculate their greatest common divisor (GCD).
            # Python's math.gcd() function is efficient for this.
            gcd_val = math.gcd(val1, val2)

            # Create a new ListNode with the calculated GCD value.
            new_node = ListNode(gcd_val)

            # Insert the new_node between 'current' and 'original_next'.
            # 1. The new_node's 'next' pointer should point to 'original_next'.
            new_node.next = original_next
            # 2. The 'current' node's 'next' pointer should now point to 'new_node'.
            current.next = new_node

            # Advance the 'current' pointer for the next iteration.
            # We move 'current' to 'original_next' (which is now 'new_node.next').
            # This is crucial because we want to calculate GCDs between the *original*
            # adjacent nodes, not between an original node and a newly inserted GCD node.
            # For example, if we have A -> B -> C, after inserting G between A and B
            # (A -> G -> B -> C), the next pair to consider is B and C.
            current = original_next 
            
        # After the loop finishes, all required GCD nodes have been inserted.
        # Return the head of the modified linked list.
        return head
