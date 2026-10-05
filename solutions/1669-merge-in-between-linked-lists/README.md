# 1669. Merge In Between Linked Lists

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/merge-in-between-linked-lists/](https://leetcode.com/problems/merge-in-between-linked-lists/)  
**Topics:** Linked List

---

## 📝 Problem Statement

You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively.

Remove `list1`'s nodes from the `ath` node to the `bth` node, and put `list2` in their place.

The blue edges and nodes in the following figure indicate the result:

*Build the result list and return its head.*

 
Example 1:

```

**Input:** list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
**Output:** [10,1,13,1000000,1000001,1000002,5]
**Explanation:** We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

```

Example 2:

```

**Input:** list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
**Output:** [0,1,1000000,1000001,1000002,1000003,1000004,6]
**Explanation:** The blue edges and nodes in the above figure indicate the result.

```

 
**Constraints:**

	- `3 4`

	- `1 4`

---

## 💻 Implementation (python3)

```py
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
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem requires removing a contiguous block of nodes from `list1` from index `a` to index `b` inclusive, and splicing `list2` into that gap.

Given the constraints:
- $1 \le a \le b < \text{list1.length} - 1$

This guarantees that:
1. The head of `list1` (index `0`) is never removed. Thus, the returned head will always be `list1`.
2. The tail of `list1` is never removed, meaning index `b + 1` always exists.

To perform the splice in $O(1)$ auxiliary space:
1. Traverse `list1` to find the node at index `a - 1` (the predecessor to the removed section) and the node at index `b + 1` (the successor to the removed section).
2. Traverse `list2` to find its last node (`tail2`).
3. Connect the node at index `a - 1` to `list2`'s head.
4. Connect `tail2` to the node at index `b + 1`.

### Step-by-Step Approach

1. Initialize a pointer `curr = list1`.
2. Iterate `idx` from `0` to `b`:
   - When `idx == a - 1`, record `node_before_a = curr`.
   - Advance `curr = curr.next`.
3. After loop finishes, `curr` points to the node at index `b + 1` (`node_after_b`).
4. Find the tail of `list2` by traversing until `tail2.next is None`.
5. Re-link:
   - `node_before_a.next = list2`
   - `tail2.next = node_after_b`
6. Return `list1`.

### Complexity Analysis

- **Time Complexity:** $O(b + m)$ where $b$ is the index in `list1` and $m$ is the number of nodes in `list2`. In the worst case, $b \le n$, making the overall time complexity $O(n + m)$, which is optimal since we only traverse the necessary parts of `list1` and `list2` once.
- **Space Complexity:** $O(1)$ auxiliary space. Only a few pointer variables (`curr`, `node_before_a`, `node_after_b`, `tail2`) are allocated; all modifications are performed in-place.

### Common Pitfalls / Mistakes

1. **Off-by-one errors with 0-indexing:**
   - Removing indices $[a, b]$ means preserving $[0, a-1]$ and $[b+1, n-1]$. Connecting the node at index `a` instead of `a - 1` is a very common bug.
2. **Memory leaks in unmanaged languages (e.g., C/C++):**
   - The removed nodes from `a` to `b` are detached from the list. In C/C++, you must iterate through the detached segment and `free`/`delete` each node to prevent memory leaks.
3. **Redundant traversals:**
   - Traversing `list1` twice (once to find index `a - 1` and again to find index `b + 1`) is unnecessary; a single pass up to `b + 1` is sufficient.

### Real Interview Follow-Up Questions

#### 1. What if $a = 0$ (the head is replaced)?
- **Answer:** If $a = 0$, the new head of the merged list becomes `list2`. We would need a dummy/sentinel node pointing to `list1`, or simply check `if a == 0: head = list2`. The rest of the logic remains the same, connecting `tail2.next` to the node at index `b + 1`.

#### 2. What if $b$ equals the length of `list1` - 1 (the tail is replaced)?
- **Answer:** Then `node_after_b` is `None`. `tail2.next = None` handles this naturally without special casing.

#### 3. How would you handle this in a concurrent environment?
- **Answer:**
  - If multiple threads are modifying disjoint sections of the linked list, fine-grained node locking (hand-over-hand locking) or lock-free linked lists using CAS (Compare-And-Swap) would be required.
  - Splicing an entire list atomically across two connection points (`a - 1` and `b + 1`) requires atomic multi-pointer updates or locking the range $[a - 1, b + 1]$ to avoid dangling references or race conditions.
