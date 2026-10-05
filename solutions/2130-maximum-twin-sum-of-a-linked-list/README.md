# 2130. Maximum Twin Sum of a Linked List

**Difficulty:** Medium  
**LeetCode Link:** [https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)  
**Topics:** Linked List, Two Pointers, Stack

---

## 📝 Problem Statement

In a linked list of size `n`, where `n` is **even**, the `ith` node (**0-indexed**) of the linked list is known as the **twin** of the `(n-1-i)th` node, if `0 

	- For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum **is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return *the **maximum twin sum** of the linked list*.

 
Example 1:

```

**Input:** head = [5,4,2,1]
**Output:** 6
**Explanation:**
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 

```

Example 2:

```

**Input:** head = [4,2,2,3]
**Output:** 7
**Explanation:**
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

```

Example 3:

```

**Input:** head = [1,100000]
**Output:** 100001
**Explanation:**
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

```

 
**Constraints:**

	- The number of nodes in the list is an **even** integer in the range `[2, 105]`.

	- `1 5`

---

## 💻 Implementation (python3)

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if not head or not head.next:
            return 0
        
        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # At this point, 'slow' points to the start of the second half of the list.
        # Step 2: Reverse the second half of the linked list in-place
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' is now the head of the reversed second half
        # Step 3: Compute maximum twin sum by traversing both halves
        max_twin_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:
            max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next
            
        # Optional Step: Restore the linked list if required by the caller (best practice)
        # We can reverse the second half again to leave the input unmodified:
        # curr, prev_restore = prev, None
        # while curr:
        #     next_node = curr.next
        #     curr.next = prev_restore
        #     prev_restore = curr
        #     curr = next_node

        return max_twin_sum
```

---

## 💡 Solution, Complexity & Interview Analysis

### Intuition & Thought Process

The problem asks for the maximum sum of twin pairs: the $i$-th node from the front paired with the $i$-th node from the back ($n - 1 - i$). 

A naive approach would be to copy all values into an array/list, which allows $O(1)$ random access to pair indices $i$ and $n - 1 - i$. However, this consumes $O(n)$ auxiliary space.

In an interview setting at top-tier companies, the interviewer will expect an in-place $O(1)$ auxiliary space solution:
1. **Find the midpoint:** Use the classic **Fast & Slow Pointer** (Tortoise and Hare) technique. Since $n$ is guaranteed to be even, when `fast` reaches `None`, `slow` points directly to the head of the second half (index $n/2$).
2. **Reverse the second half:** Invert the pointers of the second half in-place.
3. **Compare twins:** Traverse from the head of the first half and the head of the reversed second half concurrently, keeping track of the running maximum twin sum.

### Step-by-Step Approach

1. **Slow & Fast Pointer Traversal:**
   - Initialize `slow = head` and `fast = head`.
   - Advance `fast` two steps and `slow` one step until `fast` and `fast.next` are null.
   - `slow` now points to the $(n/2)$-th node.

2. **Reverse the Second Half:**
   - Use standard three-pointer iterative reversal (`prev`, `curr`, `next_node`) starting at `slow`.
   - Upon completion, `prev` points to the last node of the original list, which is now the head of the reversed second half.

3. **Calculate Maximum Twin Sum:**
   - Initialize `first_half = head` and `second_half = prev`.
   - Loop while `second_half` is not null:
     - Update `max_twin_sum = max(max_twin_sum, first_half.val + second_half.val)`.
     - Move both pointers one step forward.

4. **Return:**
   - Return `max_twin_sum`.

---

### Complexity Analysis

- **Time Complexity:** $\mathcal{O}(n)$
  - Finding the middle takes $n / 2$ steps $\rightarrow \mathcal{O}(n)$.
  - Reversing the second half takes $n / 2$ steps $\rightarrow \mathcal{O}(n)$.
  - Traversing both halves takes $n / 2$ steps $\rightarrow \mathcal{O}(n)$.
  - Overall Time Complexity: $\mathcal{O}(n)$, where $n$ is the number of nodes in the linked list.

- **Space Complexity:** $\mathcal{O}(1)$
  - No auxiliary data structures (like arrays, hash maps, or recursion stacks) are used. Pointers are manipulated strictly in-place.

---

### Common Pitfalls / Mistakes

1. **Forgetting to Clarify List Mutation:**
   - Modifying an input linked list in-place can be considered a side-effect. Always ask the interviewer: *"Am I allowed to mutate the linked list, or should I restore it before returning?"*
2. **Off-by-one with Odd Lengths:**
   - While the problem guarantees an even length, candidates often write loops that fail or get confused if $n$ could be odd. Always verify pointer conditions (`while fast and fast.next:`).
3. **Array Fallback:**
   - Implementing the $O(n)$ space approach using a Python list is acceptable as a baseline, but stopping there without mentioning the $O(1)$ space reversal will likely downgrade your score.

---

### Real Interview Follow-Up Questions

#### 1. What if the input cannot be mutated at all (e.g., read-only memory, concurrent readers)?
- **Answer:** If in-place pointer manipulation is strictly prohibited and memory is constrained, we can:
  1. Use an auxiliary array/stack to store the first $n/2$ values ($\mathcal{O}(n)$ time, $\mathcal{O}(n/2)$ space).
  2. Alternatively, use recursion to implicitly traverse the list in reverse order using the call stack ($\mathcal{O}(n)$ space).

#### 2. What if the linked list is a stream whose length $n$ is unknown until the end?
- **Answer:** We cannot locate the middle in advance without buffering or making two passes. In a streaming model with unknown $n$, we can write values to an append-only block storage / chunked array or disk, then compute twin sums via two-pointer access once the stream terminates.

#### 3. How would you handle this concurrently or in a multithreaded environment?
- **Answer:** If multiple worker threads need to read the list simultaneously, mutating pointer links (`next`) causes race conditions and data corruption. Either:
  - Make a deep copy of the second half before reversing, or
  - Protect the list with a read-write lock (`RWLock`), though reversing would require exclusive write access, blocking all concurrent readers.
