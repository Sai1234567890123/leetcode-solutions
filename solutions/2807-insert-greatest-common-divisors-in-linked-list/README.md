# 2807. Insert Greatest Common Divisors in Linked List

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/)  
**Topics:** Linked List, Math, Number Theory

---

## 📝 Problem Statement

Given the head of a linked list `head`, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the **greatest common divisor** of them.

Return *the linked list after insertion*.

The **greatest common divisor** of two numbers is the largest positive integer that evenly divides both numbers.

 
Example 1:

```

**Input:** head = [18,6,10,3]
**Output:** [18,6,6,2,10,1,3]
**Explanation:** The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

```

Example 2:

```

**Input:** head = [7]
**Output:** [7]
**Explanation:** The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

```

 
**Constraints:**

	- The number of nodes in the list is in the range `[1, 5000]`.

	- `1

---

## 💻 Implementation (python3)

```py
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
```

---

## 💡 Solution, Complexity & Interview Analysis

Detailed explanation not extracted.
